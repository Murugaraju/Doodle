from django.db import models

# Create your models here.
class Coach(models.Model):
    coach_name=models.CharField(max_length=4)
    upper=models.IntegerField()
    lower=models.IntegerField()
    middle=models.IntegerField()
    side=models.IntegerField()
    total=models.IntegerField(default=8)
    def save(self,*args,**kwargs):
        
        self.total=self.upper+self.lower+self.middle+self.side
        return super().save(*args,**kwargs)
class Ticket(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=15)
    coach_name=models.CharField(max_length=4,default=None)
    upper=models.IntegerField(default=None)
    lower=models.IntegerField(default=None)
    middle=models.IntegerField(default=None)
    side=models.IntegerField(default=None)