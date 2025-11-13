import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_greetings_page(self):
        resp = self.client.get("/users/hi/John?age=30")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"JOHN", resp.data)   # uppercased in view
        self.assertIn(b"Age: 30", resp.data)

    def test_admin_page_redirects(self):
        resp = self.client.get("/users/admin", follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"ADMINISTRATOR", resp.data)
        self.assertIn(b"Age: 45", resp.data)

if __name__ == "__main__":
    unittest.main()