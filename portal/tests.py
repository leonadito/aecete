import base64
import tempfile

from django.contrib.auth.models import Group, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Builder, PriceTable

_TINY_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk"
    "+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class PortalPermissionTests(TestCase):
    def setUp(self):
        self.builder_a_user = User.objects.create_user("builder_a", password="pass12345")
        self.builder_a = Builder.objects.create(user=self.builder_a_user, name="Construtora A")
        self.table_a = PriceTable.objects.create(
            builder=self.builder_a,
            title="Tabela A",
            description="desc",
            image=SimpleUploadedFile("a.png", _TINY_PNG, content_type="image/png"),
            drive_link="https://drive.google.com/a",
        )

        self.builder_b_user = User.objects.create_user("builder_b", password="pass12345")
        self.builder_b = Builder.objects.create(user=self.builder_b_user, name="Construtora B")

        self.broker_user = User.objects.create_user("broker", password="pass12345")
        corretores, _ = Group.objects.get_or_create(name="Corretores")
        self.broker_user.groups.add(corretores)

    def test_anonymous_redirected_from_builder_dashboard(self):
        response = self.client.get(reverse("portal:builder_dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("portal:builder_login"), response.url)

    def test_broker_login_rejects_builder_credentials(self):
        response = self.client.post(
            reverse("portal:broker_login"),
            {"username": "builder_a", "password": "pass12345"},
        )
        self.assertContains(response, "exclusivo para corretores")

    def test_builder_login_rejects_broker_credentials(self):
        response = self.client.post(
            reverse("portal:builder_login"),
            {"username": "broker", "password": "pass12345"},
        )
        self.assertContains(response, "exclusivo para construtoras")

    def test_broker_cannot_access_builder_dashboard(self):
        self.client.login(username="broker", password="pass12345")
        response = self.client.get(reverse("portal:builder_dashboard"))
        self.assertEqual(response.status_code, 403)

    def test_builder_cannot_edit_another_builders_price_table(self):
        self.client.login(username="builder_b", password="pass12345")
        response = self.client.get(reverse("portal:price_table_update", args=[self.table_a.pk]))
        self.assertEqual(response.status_code, 404)

    def test_builder_dashboard_only_lists_own_tables(self):
        self.client.login(username="builder_b", password="pass12345")
        response = self.client.get(reverse("portal:builder_dashboard"))
        self.assertNotContains(response, "Tabela A")

    def test_broker_can_view_all_active_tables_without_edit_links(self):
        self.client.login(username="broker", password="pass12345")
        response = self.client.get(reverse("portal:broker_price_table_list"))
        self.assertContains(response, "Tabela A")
        self.assertNotContains(response, "Editar")
