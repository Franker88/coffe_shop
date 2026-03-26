from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=255, verbose_name='Product name')
    description = models.TextField(max_length=300, verbose_name='Product description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Product price')
    available = models.BooleanField(default=True, verbose_name='Available')
    image = models.ImageField(upload_to='assets', null=True, blank=True, verbose_name='Product image')

    def __str__(self):
        return self.name