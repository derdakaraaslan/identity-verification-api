# Generated by Django 3.2 on 2022-07-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0021_identity_bio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='qrcode',
            field=models.ImageField(default='no image', upload_to='qrcode'),
        ),
    ]
