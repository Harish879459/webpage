from django.db import models

# Create your models here.
class Cab(models.Model):
   cab_id = models.AutoField(auto_created=True, primary_key=True)
   description = models.CharField(max_length=100)
   image = models.FileField(upload_to="static/images/cab/")

   class Meta:
       db_table = "cab"
