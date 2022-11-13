# Generated by Django 3.2 on 2022-07-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0015_auto_20220722_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='birthdate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='identity',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='identity',
            name='documentNumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='identity',
            name='documentType',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='identity',
            name='expiryDate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='identity',
            name='givenNames',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='identity',
            name='nationalityCode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='identity',
            name='personalNumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='identity',
            name='personalNumber2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='identity',
            name='sex',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='identity',
            name='surnames',
            field=models.CharField(max_length=40),
        ),
    ]