# Generated by Django 3.2 on 2022-07-22 12:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0011_auto_20220722_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='birthdate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='country',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='documentNumber',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='documentType',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='expiryDate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='givenNames',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='id',
            field=models.UUIDField(default=uuid.UUID('654c0a3a-363e-4571-99d7-af01bced7bfc'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='identity',
            name='nationalityCode',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='personalNumber',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='personalNumber2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='identity',
            name='sex',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='process',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f68c88b4-ebd7-46e7-9672-af5bd42d9a69'), primary_key=True, serialize=False),
        ),
    ]
