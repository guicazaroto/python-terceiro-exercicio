# Generated by Django 4.2.7 on 2023-11-14 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=20)),
                ('contato', models.CharField(max_length=15)),
                ('aluguel', models.CharField(max_length=20)),
                ('condominio', models.CharField(max_length=20)),
            ],
        ),
    ]
