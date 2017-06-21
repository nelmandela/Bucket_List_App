import unittest
from app import app

class BucketListTest(unittest.TestCase):
    """ Test for bucket List"""
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_login_page_displays(self):
        response = self.app.get("/")
        self.assertIn(b'login', response.data)

    def test_signup_page_displays(self):
        response = self.app.get("/signup")
        self.assertIn(b'Sign Up', response.data)

    def test_signup(self):
        response = self.app.post("/signup")
        #add test to see if signup works

    def test_signin(self):
        response = self.app.post("/login")
        #add test to see if login works
