# Generated by Django 4.0.2 on 2022-02-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, height_field='300', null=True, upload_to='blog', width_field='200'),
        ),
    ]