from django.test import TestCase
from home.models import Mesaj


class PostTestCase(TestCase):
    def testPost(self):
        post = Mesaj(nume="My Name", email="MyEmail", numar_telefon="MuPhone")
        self.assertEqual(post.nume, "My Name")
        self.assertEqual(post.email, "MyEmail")
        self.assertEqual(post.numar_telefon, "MuPhone")