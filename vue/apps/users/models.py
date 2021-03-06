from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=6, choices=(('male', u'男'),('female', '女')), default='female', verbose_name='性别')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username