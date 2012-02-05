from django.test import TestCase
from public.models import Public

class PublicManagerTest(TestCase):
    def test_get_must_popular(self):
        """
        Get must popular Publics
        """
        pub = Public.objects.must_popular()
         
        #FIXME: error
        pass
        self.assertEqual(pub, None)

    def test_lastest_five(self):
            """
            Tests that 1 + 1 always equals 2.
            """
            self.assertEqual(1 + 1, 2)
