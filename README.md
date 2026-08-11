# AICITI — site institucional

Refatoração do site da AICITI (Associação das Imobiliárias e Corretores de Imóveis de
Tramandaí e Imbé). Ver [PRD.md](PRD.md) para os requisitos completos e [CLAUDE.md](CLAUDE.md)
para orientações de arquitetura.

## Stack

Django + Tailwind CSS (CLI standalone, v4) + Alpine.js + HTMX + SQLite, containerizado com Docker
para deploy em VPS.

## Desenvolvimento local

Pré-requisitos: Python 3.12.

```bash
# 1. Ambiente virtual e dependências
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements-dev.txt

# 2. Banco de dados
python manage.py migrate
python manage.py seed_all      # popula diretoria, benefícios, FAQ, parceiros e o post real do blog (com fotos/logos)
python manage.py createsuperuser

# 3. CSS (rodar em paralelo ao servidor, em outro terminal)
# Baixe o binário standalone do Tailwind CLI (v4.3.3) compatível com seu SO em:
# https://github.com/tailwindlabs/tailwindcss/releases
./tailwindcss.exe -i ./static/src/tailwind/input.css -o ./static/css/output.css --watch

# 4. Servidor de desenvolvimento
python manage.py runserver
```

Site em `http://127.0.0.1:8000/`, admin em `http://127.0.0.1:8000/admin/`.

### Rodar os testes

```bash
python manage.py test
```

## Deploy (Docker / VPS)

```bash
cp .env.example .env    # preencher com valores reais antes de subir em produção
docker compose up --build -d
```

O `Dockerfile` builda o CSS do Tailwind em um estágio separado (binário standalone Linux,
sem Node/npm) e gera a imagem final Python com Django + gunicorn + WhiteNoise (sem nginx
separado). O `docker-compose.yml` mantém volumes nomeados para o banco SQLite (`db_data`) e
uploads (`media_data`), que sobrevivem a rebuilds da imagem.

TLS/reverse proxy na frente do container (ex.: Caddy ou nginx) fica a cargo da configuração
da VPS — não faz parte deste repositório.

## Estrutura dos apps

- `pages` — Home, Sobre, Benefícios, Dúvidas (models `BoardMember`, `Benefit`, `FAQItem`).
- `partners` — Parceiros comerciais e imobiliárias associadas (model `Partner`, campo `kind`).
- `blog` — Sistema de blog (model `Post`), com paginação via HTMX.
- `contact` — Formulário de contato (model `ContactMessage`), envio via HTMX + e-mail.

Todo o conteúdo institucional (diretoria, benefícios, FAQ, parceiros) é editável pelo
Django Admin (`/admin/`) e pode ser re-semeado a qualquer momento com `seed_all`
(idempotente — não duplica registros existentes).

## Imagens

- `static/img/` — identidade visual do site (logo, favicon, foto do hero, banner interno),
  extraída do site atual (aiciti.com.br) e versionada no repositório.
- `seed_media/` — fotos da diretoria, logos de parceiros/imobiliárias associadas, imagens dos
  benefícios e a capa do post real do blog, também extraídas do site atual. São versionadas no
  git e copiadas para `media/` pelos comandos `seed_*` na primeira execução (não sobrescrevem
  uma imagem já trocada manualmente pelo Admin).
- `media/` — uploads feitos pelo Admin (novas fotos, logos, posts); não é versionado, é um
  volume persistente no container Docker.
