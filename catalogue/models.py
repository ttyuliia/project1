from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Good(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    description = models.TextField(max_length=512)
    photo = models.FileField(upload_to='goods_photo/')
    size = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
