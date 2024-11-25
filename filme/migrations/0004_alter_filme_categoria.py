# Generated by Django 4.2.16 on 2024-11-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0003_rename_vusualizacoes_filme_visualizacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ANALISES', 'Análises'), ('PROGRAMACAO', 'Programação'), ('APRESENTACAO', 'Apresentação'), ('OUTROS', 'Outros')], max_length=50),
        ),
    ]