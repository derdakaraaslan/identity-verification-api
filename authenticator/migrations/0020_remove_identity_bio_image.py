# Generated by Django 3.2 on 2022-07-27 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0019_identity_bio_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identity',
            name='bio_image',
        ),
    ]
