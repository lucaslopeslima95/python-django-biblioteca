# Generated by Django 4.2.2 on 2023-06-06 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_alter_livro_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
