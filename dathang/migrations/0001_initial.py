# Generated by Django 2.2.6 on 2019-12-01 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address', models.CharField(default='', max_length=255)),
                ('order_description', models.TextField(default='')),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
