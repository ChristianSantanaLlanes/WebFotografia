# Generated by Django 4.0.2 on 2022-02-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galerya', '0003_alter_fotos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
