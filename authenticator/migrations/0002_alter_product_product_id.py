# Generated by Django 3.2 on 2022-07-05 10:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('040eda56-cc02-4f31-a040-8d6b124eb339')),
        ),
    ]
