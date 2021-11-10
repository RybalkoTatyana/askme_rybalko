from django.db import models


# Create your models here.
class Questions(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    is_active = models.BooleanField(default=True, verbose_name='Question active')
    title = models.CharField(max_length=50, verbose_name='Title')
    text = models.TextField(verbose_name='Question text')
    rating = models.IntegerField(default=0, verbose_name='Rating')


class Tags(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(default='404', max_length=50, verbose_name='Tag')


class Answers(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    text = models.TextField(verbose_name='Question text')
    status = models.BooleanField(default=False, verbose_name='Status')
