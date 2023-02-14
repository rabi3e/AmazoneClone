from django.db import models
from taggit.managers import TaggableManager

FLAGS_TYPES = (
    ('N', 'New')
    ('F', 'Feature')
    ('S', 'Sale')
    )

class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    sku = models.IntegerField()
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=20000)
    flag = models.CharField(max_length=1, choices=FLAGS_TYPES)
    brand = models.ForeignKey('Brand',related_name='product_brand', on_delete=models.)
