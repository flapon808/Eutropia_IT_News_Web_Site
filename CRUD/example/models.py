from django.db import models

# Create your models here.
class registration(models.Model):
    eid = models.CharField(max_length= 20)
    ename = models.CharField(max_length=200)
    email = models.EmailField()
    ephone = models.IntegerField(max_length=20)

def __str__ (self):
    return "%s"  %(self.ename) 

class meta:
    db_table = "employee"