# -*-coding:UTF-8-*-
from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField('productname',max_length=64) #产品名称
    productdesc = models.CharField('productdesc',max_length=200) #产品描述
    producter = models.CharField('producter',max_length=200) # 产品负责人
    create_time = models.DateTimeField('create_time',auto_now = True) #创建时间，自动获取当前时间

class Meta:
    verbose_name = 'Product Manage'
    verbose_name_plural = 'Product Manage'

def __str__(self):
    return self.productname