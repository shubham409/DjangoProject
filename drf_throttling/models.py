from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    # help(id)
    name = models.CharField(max_length=50 ,default=f'Student{id.value_to_string}')
    roll = models.CharField(max_length=10 , default=str(100))
    branch = models.CharField(max_length=30 , default='cse')