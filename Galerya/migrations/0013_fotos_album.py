# Generated by Django 4.0.2 on 2022-02-10 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Galerya', '0012_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotos',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Galerya.album'),
        ),
    ]
