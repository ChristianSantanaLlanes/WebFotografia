# Generated by Django 4.0.2 on 2022-02-09 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Galerya', '0007_alter_fotos_create_remove_fotos_seccion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotos',
            name='seccion',
        ),
        migrations.AddField(
            model_name='fotos',
            name='seccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Galerya.secciones'),
        ),
    ]