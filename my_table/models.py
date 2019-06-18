from django.db import models

# Create your models here.
class Area(models.Model):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Province(models.Model):
    id      = models.AutoField(primary_key=True)
    area_id = models.ForeignKey(Area                ,on_delete = models.CASCADE)
    name    = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tourist_Attraction(models.Model):
    id      = models.AutoField(primary_key=True)
    prov_id = models.ForeignKey(Province            ,on_delete = models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Travel_Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='plans', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
        
class My_Table(models.Model):
    id      = models.AutoField(primary_key=True)
    plan_id = models.ForeignKey(Travel_Plan         , on_delete=models.CASCADE)
    tour_id = models.ForeignKey(Tourist_Attraction  , on_delete=models.CASCADE)
    date    = models.DateTimeField(auto_now=False   , auto_now_add=False)
    note    = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)
