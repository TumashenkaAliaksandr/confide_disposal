# Generated by Django 4.2.6 on 2023-10-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider', verbose_name='Photo'),
        ),
    ]
