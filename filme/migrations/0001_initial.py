# Generated by Django 4.2.16 on 2024-11-09 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_filmes')),
                ('descricao', models.TextField(max_length=10000)),
                ('categoria', models.CharField(choices=[('ANALISES', 'Análises'), ('PROGRAMACAO', 'Programação'), ('APRESENTACAO', 'Apresentação'), ('OUTROS', 'Outros')], max_length=30)),
                ('vusualizacoes', models.ImageField(default=0, upload_to='')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
