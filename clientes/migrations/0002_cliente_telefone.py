# Generated by Django 4.2.1 on 2023-06-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
