from django.db import models

# Create your models here.
class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   inventory = models.SmallIntegerField(default=5) 

   def __str__(self):
      return self.title


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name
    
