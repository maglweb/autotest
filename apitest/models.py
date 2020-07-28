# -*-coding:UTF-8-*-
from django.db import models
from product.models import Product
#
# # Create your models here.
# class Product(models.Model):
#     productname = models.CharField('productname',max_length=64) #��Ʒ����
#     productdesc = models.CharField('productdesc',max_length=200) #��Ʒ����
#     producter = models.CharField('producter',max_length=200) # ��Ʒ������
#     create_time = models.DateTimeField('create_time',auto_now = True) #����ʱ�䣬�Զ���ȡ��ǰʱ��
#
# class Meta:
#     verbose_name = 'Product Manage'
#     verbose_name_plural = 'Product Manage'
#
# def __str__(self):
#     return self.productname

class Apitest(models.model):
