# Generated by Django 4.2.6 on 2023-10-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_disposal_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='Photo')),
                ('is_main', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
            },
        ),
        migrations.AlterField(
            model_name='disposal',
            name='image',
            field=models.ImageField(upload_to='disposal/', verbose_name='Photo'),
        ),
    ]