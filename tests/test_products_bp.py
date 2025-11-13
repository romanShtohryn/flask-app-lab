import unittest
from app import app

class ProductsBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_products_list(self):
        resp = self.client.get("/products/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Products", resp.data)
        self.assertIn(b"Flask Course", resp.data)
        self.assertIn(b"Python Book", resp.data)

if __name__ == "__main__":
    unittest.main()