# Generated by Django 3.2.23 on 2023-12-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
