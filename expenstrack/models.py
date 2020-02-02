from django.db import models
from django.core.exceptions import ValidationError
from myuser.models import MyUser
def validateTitle(value):
    if '@' in value or '#' in value or '$' in value or '%' in value:
        raise ValidationError("the special symbol are not allowed in title")
    else:
        return value

def greaterThanFive(value):
    if len(value)>5:
        return value
    else:
        raise ValidationError("must be greater than 5")

def amountValidation(value):
    if value>0:
        return value
    else:
        raise ValidationError("amount must be greater than 0")

class IncomeManager(models.Manager):

    def greaterThan(self,value):
        return self.filter(amount__gte=value)

class CommonInfo(models.Model):
    title = models.CharField(max_length=100, validators=[validateTitle, greaterThanFive])
    amount = models.FloatField()
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Income(CommonInfo):
    source = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='income/', blank=True, null=True)
    objects = IncomeManager()

    def __str__(self):
        return self.title



class ExpenseManager(models.Manager):

    def greaterThan(self,value):
        return self.filter(amount__gte=value)



class Expense(CommonInfo):
    image = models.ImageField(upload_to='expenses/', blank=True, null=True)
    objects = ExpenseManager()

    def __str__(self):
        return self.title


