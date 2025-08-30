from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='games/')
    old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title