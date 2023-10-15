from django.db import models


class Disposal(models.Model):
    """Disposal model"""
    name = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Price')
    image = models.ImageField(upload_to='disposal_photo/', verbose_name='Photo')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Disposal"
        verbose_name_plural = "Disposal"


class Slider(models.Model):
    """Slider model"""
    name = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='slider', verbose_name='Photo')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"