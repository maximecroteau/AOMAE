from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    old_price = models.IntegerField(blank=True, null=True, default=None)
    price = models.IntegerField()
    picture = models.ImageField(blank=True, upload_to="static/images/bdd/")
    stars = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Produit"
        ordering = ['name']

    def __str__(self):
        return self.name

