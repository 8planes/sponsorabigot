from django.db import models

class Pledge(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=32, blank=False)
    email = models.EmailField(unique=True, db_index=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirm_date = models.DateTimeField(null=True)
    confirm_code = models.CharField(
        max_length=255, blank=False, unique=True, db_index=True)

