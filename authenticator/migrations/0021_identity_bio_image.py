# Generated by Django 3.2 on 2022-07-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0020_remove_identity_bio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='bio_image',
            field=models.TextField(default='No image'),
        ),
    ]
