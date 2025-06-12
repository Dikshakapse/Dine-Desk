from django.db import models

# Create your models here.
class DailyMenu(models.Model):
    date = models.DateField(auto_now_add=True)
    full_tiffin_description = models.TextField()
    full_tiffin_price = models.DecimalField(max_digits=6, decimal_places=2)
    half_tiffin_type1_description = models.TextField()
    half_tiffin_type1_price = models.DecimalField(max_digits=6, decimal_places=2)
    half_tiffin_type2_description = models.TextField()
    half_tiffin_type2_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Menu for {self.date}"