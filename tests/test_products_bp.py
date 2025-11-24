from app import create_app, db
import unittest

class ProductsBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app = app
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_products_list(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()