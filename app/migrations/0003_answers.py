# Generated by Django 3.2.9 on 2021-11-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Question text')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
    ]
