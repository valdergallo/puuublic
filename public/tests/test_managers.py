from django.test import TestCase
from public.models import Public
from django_dynamic_fixture import G


class PublicManagerTest(TestCase):
    def setUp(self):
        G(Public, n=20)

    def test_get_must_popular(self):
        pub = Public.objects.must_popular()
        self.assertEqual(pub.count(), 10)

    def test_get_last_five(self):
        pub = Public.objects.lastest_five()
        self.assertEqual(pub.count(), 5)
