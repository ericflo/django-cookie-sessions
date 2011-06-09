from django.test import TestCase

from django.contrib.sessions.tests import SessionTestsMixin

from cookiesessions.engine import SessionStore as CookieSession

class CacheDBSessionTests(SessionTestsMixin, TestCase):
    backend = CookieSession
    
    def test_save(self):
        """
        This test tested exists() in the other session backends, but that
        doesn't make sense for us.
        """
        pass