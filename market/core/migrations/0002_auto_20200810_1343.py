# Generated by Django 2.2.15 on 2020-08-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='national_ID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=13, null=True),
        ),
    ]