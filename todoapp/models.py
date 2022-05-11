from django.db import models


class UserRegister(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'registerinfo'


class UserLogin(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=56)

    class Meta:
        db_table = 'logininfo'


class TodoList(models.Model):
    text = models.CharField(max_length=100)

    class Meta:
        db_table = 'todoinfo'
