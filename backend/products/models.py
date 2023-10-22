# Import models from Django
from django.db import models

# Import uuid for unique id
import uuid

# Import settings
from django.contrib.auth.models import User


# Create a Product model
class Product(models.Model):
    # Use UUID as the primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Attach an user to the product
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)

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
