from django.db import models

# Create your models here.
class Files(models.Model):
    name = models.CharField(verbose_name='文件名',max_length=32)
