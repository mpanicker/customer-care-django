from django.db import models

# Create your models here.

class AccountInfo(models.Model):
    account_id = models.AutoField(primary_key=True)
    cust_name = models.TextField(max_length=200)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    user_id = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=12)
    devices = models.ForeignKey('Device',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.account_id)

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    type = models.TextField(max_length=20) #iphone, samsung etc
    model_number = models.CharField(max_length=10)
    imei = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.device_id)
