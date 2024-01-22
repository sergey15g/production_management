# production/models.py
from django.db import models

class Nomenclature(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)

class Group(models.Model):
    name = models.CharField(max_length=255)

class ProductionArea(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class NomenclaturePrice(models.Model):
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.CASCADE)
    production_area = models.ForeignKey(ProductionArea, on_delete=models.CASCADE)
