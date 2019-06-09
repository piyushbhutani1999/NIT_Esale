from django.db import models

from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

from accounts.models import User


class Product(models.Model):
    title = models.CharField(max_length = 10)
    slug = models.SlugField(unique = True, blank = True)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(max_length=200)
    price = models.PositiveIntegerField(default = 0)
    featured = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'images/', null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  "/product/{slug}/".format(slug = self.slug)
    
def product_pre_save_register(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_register,sender = Product)