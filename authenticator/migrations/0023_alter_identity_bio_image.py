# Generated by Django 3.2 on 2022-07-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0022_process_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='bio_image',
            field=models.ImageField(default='No image', upload_to='bio'),
        ),
    ]
