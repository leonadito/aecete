# syntax=docker/dockerfile:1

# ---- Stage 1: build the Tailwind CSS with the standalone CLI (no Node/npm) ----
FROM debian:bookworm-slim AS tailwind-builder
ARG TAILWIND_VERSION=v4.3.3
WORKDIR /build

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sLo /usr/local/bin/tailwindcss \
        "https://github.com/tailwindlabs/tailwindcss/releases/download/${TAILWIND_VERSION}/tailwindcss-linux-x64" \
    && chmod +x /usr/local/bin/tailwindcss

COPY static/src/tailwind ./static/src/tailwind
COPY templates ./templates
COPY pages/templates ./pages/templates
COPY partners/templates ./partners/templates
COPY blog/templates ./blog/templates
COPY contact/templates ./contact/templates

RUN tailwindcss -i ./static/src/tailwind/input.css -o ./static/css/output.css --minify


# ---- Stage 2: the Django application ----
FROM python:3.12-slim AS final
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=tailwind-builder /build/static/css/output.css ./static/css/output.css

RUN mkdir -p /app/db /app/media /app/staticfiles \
    && python manage.py collectstatic --noinput --ignore=src

EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
