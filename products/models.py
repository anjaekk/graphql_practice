from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'product_types'

class Product(models.Model):
    name            = models.CharField(max_length=45)
    price           = models.DecimalField(max_digits=18, decimal_places=2)
    description     = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    product_type    = models.ForeignKey('ProductType', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'