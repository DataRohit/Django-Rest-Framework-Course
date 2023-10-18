# Import models from Django
from django.db import models

# Import uuid for unique id
import uuid


# Create a Product model
class Product(models.Model):
    # Use UUID as the primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Fields of the model
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10_000)
