# Generated by Django 4.1.6 on 2023-12-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_thirdparty_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='conclusion',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(max_length=250),
        ),
    ]
