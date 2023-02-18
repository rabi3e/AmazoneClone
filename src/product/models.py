from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.text import slugify

from django.contrib.auth.models import User
from django.utils.translation import gettext as _

FLAGS_TYPES = (
    ('N', 'New'),
    ('F', 'Feature'),
    ('S', 'Sale')
    )

class Product(models.Model):
    name = models.CharField(_('Title'),max_length=120)
    image = models.ImageField(_('image'),upload_to='products')
    price = models.FloatField(_('price'))
    sku = models.IntegerField(_('sku'))
    subtitle = models.CharField(_('subtitle'),max_length=300)
    description = models.TextField(_('description'),max_length=20000)
    flag = models.CharField(_('flag'),max_length=1, choices=FLAGS_TYPES)
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'),related_name='product_brand', on_delete=models.SET_NULL, null=True,blank=True)
    tag = TaggableManager()
    slug = models.SlugField(null=True,blank=True)
    
    class Meta :
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
           
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Product, self).save(*args, **kwargs) # Call the real save() method

class Brand(models.Model):
    name = models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='brand')
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    
class ProductImages(models.Model):
    product= models.ForeignKey(Product,related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')
    
    def __str__(self):
        return str(self.product)    
    
class ProductReview(models.Model):
    user=models.ForeignKey(User,verbose_name=_('user'),related_name='review_author', on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,verbose_name=_('product'),related_name='product_review' , on_delete=models.CASCADE)
    rate = models.IntegerField(_('rate'))
    review = models.TextField(_('review'),max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user) 
       