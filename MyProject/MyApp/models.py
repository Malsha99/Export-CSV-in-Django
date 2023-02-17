
from django.db import models

# Create your models here.
class Post(models.Model):
    FirstName = models.CharField("Enter First Name", max_length=50)
    LastName = models.CharField("Enter Last Name", max_length=50)
    City = models.CharField("Enter City", max_length=50)

# provide a string representation
def _str_(self):
    return str(self.FirstName)



