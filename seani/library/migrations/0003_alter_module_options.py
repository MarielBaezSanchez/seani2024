# Generated by Django 5.0.2 on 2024-02-16 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_image_text_question_question_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'pregunta', 'verbose_name_plural': 'preguntas'},
        ),
    ]
