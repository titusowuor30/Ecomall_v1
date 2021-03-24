from django.db import models
import random,math

class Pay_method_category(models.Model):
    title=models.CharField(max_length=100,help_text='E.G Bank,Mpesa,Paypal')
    slug=models.SlugField(max_length=255,default='pay-url-'+(str(random.random()*1000000000000).__floor__()))

class Billing_info(models.Model):
    category=models.ForeignKey(Pay_method_category,on_delete=models.CASCADE,related_name='categoriees')
    account_number=models.CharField(max_length=20)
    pay_bill=models.IntegerField(max_length=20)
    till_no=models.IntegerField(max_length=10)



