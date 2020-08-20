from django.db import models
from cab.models import Cab
from customer.models import Customer
# Create your models here.
class Book(models.Model):
    book_id = models.AutoField(auto_created=True, primary_key=True)
    cab=models.ForeignKey(Cab,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    time=models.CharField(max_length=20)
    date=models.CharField(max_length=10)
    class Meta:
        db_table = "book"
