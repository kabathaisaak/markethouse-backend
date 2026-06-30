from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200)
    summary = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=200)
    detail = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit = models.CharField(max_length=50)

    image = models.ImageField(
        upload_to="products/"
    )

    stock = models.PositiveIntegerField(default=0)

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name