from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Luxury Wool Rug",
            category="rug",
            description="A beautiful handmade wool rug.",
            price=299.99,
            stock_quantity=50
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Luxury Wool Rug")
        self.assertEqual(self.product.price, 299.99)
