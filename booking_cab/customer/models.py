from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    class Meta:
        db_table = "customer"
