# Generated by Django 3.2.3 on 2022-01-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
