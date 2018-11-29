from django.db import models

from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    # 引用django内置的auth用户管理,就不用自己再写字段了,只需要把没有的补充上就行了
    phone = models.CharField(max_length=11,null=True, unique=True)
    def __str__(self):
        return self.username