from rest_framework.validators import UniqueValidator
from products.models import Product


unique_title_validator = UniqueValidator(
    message="A product with this title already exists.", queryset=Product.objects.all()
)
