# Generated by Django 4.2.2 on 2023-06-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(max_length=31),
        ),
    ]
