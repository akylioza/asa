from django.contrib.admin import site
from . import models
# Register your models here.
site.register(models.Cloth)
site.register(models.Tag)
site.register(models.Customer)
site.register(models.Order)
