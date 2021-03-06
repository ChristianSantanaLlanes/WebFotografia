# Generated by Django 4.0.2 on 2022-02-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_remove_post_categorias_post_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('web', models.CharField(blank=True, max_length=50, null=True)),
                ('comentario', models.TextField(max_length=1000)),
            ],
        ),
    ]
