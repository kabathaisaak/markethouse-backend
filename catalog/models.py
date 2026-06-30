from django.db import models


class Store(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    tagline = models.CharField(max_length=150)

    summary = models.TextField()

    logo = models.ImageField(
        upload_to="stores/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Category(models.Model):

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="products"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to="products/"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    available = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name