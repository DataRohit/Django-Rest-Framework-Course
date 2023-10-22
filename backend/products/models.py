# Import models from Django
from django.db import models

# Import uuid for unique id
import uuid


# Create a Product model
class Product(models.Model):
    def __str__(self):
        return self.title

    # Use UUID as the primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Fields of the model
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(max_length=120)

    # Property of the model
    @property
    def sale_price(self):
        return round(float(self.price) * 0.8, 2)

    @property
    def discount(self):
        return round(float(self.price) * 0.2, 2)
