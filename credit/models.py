from django.db import models
from random import randint


class Client(models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20,default='Кыргызстан')
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'


class Account(models.Model):
    number = models.CharField(max_length=16, unique=True)
    account_type = models.IntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="accounts")

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField()
    date = models.DateField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="credits")

    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'



