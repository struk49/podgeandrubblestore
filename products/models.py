from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model Product contains the detailed product information
    with foreign keys to the related category models
    """

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    sku = models.CharField(
        max_length=254)
    name = models.CharField(
        max_length=254)
    product_description = models.TextField()
    sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True)
    gender = models.CharField(max_length=20)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    image = models.ImageField(
        blank=True,
        null=True)

    def __str__(self):
        return self.name
