from django.db import models

# Create your models here.


#class Destination:
class Destination(models.Model):   # for models in DB
    '''
    id : int   in DB auto create
    name : str
    desc : str
    reviews : str
    days : str
    offer : bool
    '''

# for model
    name = models.CharField(max_length=100)
    desc = models.TextField()
    reviews = models.TextField()
    days = models.TextField()
    offer = models.BooleanField(default=False)
