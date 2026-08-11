from pathlib import Path

from django.conf import settings
from django.core.files import File

SEED_MEDIA_ROOT = Path(settings.BASE_DIR) / "seed_media"


def attach_image(instance, field_name, subdir, filename):
    """Attach a committed seed image to an ImageField, unless one is already set.

    Source files live in `seed_media/<subdir>/<filename>` (versioned in git) and are
    copied into MEDIA_ROOT via the field's storage the first time a seed command runs.
    """
    field = getattr(instance, field_name)
    if field:
        return

    path = SEED_MEDIA_ROOT / subdir / filename
    if not path.exists():
        return

    with open(path, "rb") as f:
        field.save(filename, File(f), save=True)
