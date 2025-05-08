from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("rug", "Rug"),
        ("cushion", "Cushion"),
        ("puff", "Puff"),
        ("carpet", "Carpet"),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
