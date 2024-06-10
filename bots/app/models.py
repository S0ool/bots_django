from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Robot(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='robots')

    def __str__(self):
        return self.name


class Shop_robots(models.Model):
    name = models.CharField(max_length=255)
    robot = models.ManyToManyField(Robot, related_name='shop_robots')

    def __str__(self):
        return self.name