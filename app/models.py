from django.db import models
from django.template.defaultfilters import slugify

from user.models import Customer


class Base(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, *kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Valyuta(Base):
    pass


class Categories(Base):
    image = models.ImageField(upload_to="categories", null=True, blank=True)


class Product(Base):
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="product", null=True)
    see_count = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    valyuta = models.ForeignKey(Valyuta, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    count = models.IntegerField()




