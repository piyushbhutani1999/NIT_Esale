from django.db import models
from datetime import datetime  
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

from accounts.models import User

CATEGORY_CHOICES = (
    ('electronic','Electronic'),
    ('stationary', 'Stationary'),
    ('roomdecor','Room Decor'),
    ('vehicle','Vehicle'),
    ('job','Job'),
    ('other','Other'),
)
class Product(models.Model):
    title = models.CharField(max_length = 40)
    slug = models.SlugField(unique = True, blank = True)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField(default = 0)
    featured = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'images/', null = True)
    date = models.DateTimeField(default=datetime.now, blank=True, null = True)
    college = models.CharField(blank = True, null = True, max_length = 30)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  "/product/{slug}/".format(slug = self.slug)
    
def product_pre_save_register(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_register,sender = Product)