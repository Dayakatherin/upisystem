from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Transactions(models.Model):
    PAYMENT_CHOICES = ( ('COD', 'Cash on delivery'),('ONLINE', 'upi'),)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_amount = models.CharField(max_length=25, default=700)
    order_payment_id = models.CharField(max_length=100, default='')
    mode_of_payment = models.CharField(max_length=100, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return "ID: " + str(self.id) 