# Generated by Django 4.0.2 on 2022-02-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galerya', '0004_alter_fotos_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotos',
            name='create',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fotos',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
