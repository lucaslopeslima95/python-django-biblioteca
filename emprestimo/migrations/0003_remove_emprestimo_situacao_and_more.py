# Generated by Django 4.2.1 on 2023-06-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_emprestimo_situacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='situacao',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='status_emprestimo',
            field=models.IntegerField(choices=[(1, 'Em Dia'), (2, 'Atrasado'), (3, 'Concluido')], default=1),
        ),
    ]
