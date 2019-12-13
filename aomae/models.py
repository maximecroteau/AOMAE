from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    picture = models.ImageField(blank=True)
    stars = models.IntegerField(blank=True)

    class Meta:
        verbose_name = "Produit"
        ordering = ['name']

    def __str__(self):
        return self.name

