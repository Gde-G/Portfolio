# Generated by Django 4.1.6 on 2023-12-13 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_project_conclusion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='conclusion',
        ),
    ]
