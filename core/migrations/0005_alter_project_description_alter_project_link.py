# Generated by Django 4.1.6 on 2023-02-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_testimonial_punctuation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(max_length=120),
        ),
    ]
