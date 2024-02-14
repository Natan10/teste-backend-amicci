from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


# Varejista
class Retailer(models.Model):
    name = models.CharField(max_length=165)

# Fornecedor
class Vendor(models.Model):
    name = models.CharField(max_length=165)
    retailer = models.ForeignKey(Retailer, on_delete=models.SET_NULL, null=True)


class Briefing(models.Model):
    name = models.CharField(max_length=165)
    responsible = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    available = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)