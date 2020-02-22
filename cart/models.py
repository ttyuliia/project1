from django.db import models
from catalogue.models import Good
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    quantity = models.PositiveIntegerField()
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class Phone_num(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
