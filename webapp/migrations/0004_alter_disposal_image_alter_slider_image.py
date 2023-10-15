# Generated by Django 4.2.6 on 2023-10-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_slider_alter_disposal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposal',
            name='image',
            field=models.ImageField(upload_to='disposal_photo/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider_photo/', verbose_name='Photo'),
        ),
    ]
