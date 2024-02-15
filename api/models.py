from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name

# Varejista
class Retailer(models.Model):
    name = models.CharField(max_length=165)

    def __str__(self) -> str:
        return self.name

# Fornecedor
class Vendor(models.Model):
    name = models.CharField(max_length=165)
    retailer = models.ForeignKey(Retailer, on_delete=models.SET_NULL, null=True, related_name='vendors')

    def __str__(self) -> str:
        return self.name

class Briefing(models.Model):
    name = models.CharField(max_length=165)
    responsible = models.CharField(max_length=255)
    available = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name