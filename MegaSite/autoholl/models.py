from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    short_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Company"

class Cars(models.Model):
    name = models.CharField(max_length=20)
    power = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    compony = models.ForeignKey(Company, on_delete=models.CASCADE, to_field="name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cars"