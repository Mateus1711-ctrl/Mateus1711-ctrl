# Generated by Django 4.2.1 on 2024-04-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0006_formulario_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta_de_texto', models.TextField(blank=True, max_length=2000, null=True)),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='pergunta',
        ),
    ]