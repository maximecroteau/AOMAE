from django.db import models

# Create your models here.


class Products(models.Model):
    Homme = "Homme"
    Femme = "Femme"
    Unisex = "Unisex"

    gender_choice = [
        (Homme, "Homme"),
        (Femme, "Femme"),
        (Unisex, "Unisex"),
    ]

    SML = "SML"
    Numbers = "Numbers"
    Words = "Words"
    size_choice = [
        (SML, "SML"),
        (Numbers, "Numbers"),
        (Words, "Words"),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    picture = models.ImageField(blank=True, upload_to="static/images/bdd/")
    color = models.ManyToManyField('Color')
    gender = models.CharField(choices=gender_choice, max_length=7, default="Unisex")
    description = models.CharField(blank=True, max_length=600, default="Pas de description actuellement")
    size_type = models.CharField(choices=size_choice, max_length=7, default="Words")
    stars = models.IntegerField(blank=True, null=True, default=None)

    def get_colors(self):
        return "\n".join([c.color for c in self.color.all()])

    class Meta:
        verbose_name = "Produit"
        ordering = ['name']

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Couleur"
        ordering = ['color']

    def __str__(self):
        return self.color


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1200)

    class Meta:
        verbose_name = "Contact"
        ordering = ['name']
