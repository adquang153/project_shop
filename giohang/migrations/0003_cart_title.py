# Generated by Django 2.2.6 on 2019-12-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giohang', '0002_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]