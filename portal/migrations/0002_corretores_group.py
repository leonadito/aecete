from django.db import migrations


def create_corretores_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.get_or_create(name="Corretores")


def delete_corretores_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name="Corretores").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(create_corretores_group, delete_corretores_group),
    ]
