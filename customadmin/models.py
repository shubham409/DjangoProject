from django.db import models

# Create your models here.

class Collegs(models.Model):
    name = models.CharField(max_length=200)
    total_students = models.IntegerField(default=1000)
    branches = models.IntegerField(default=6)
    location = models.CharField(max_length=100 ,default="New Delhi")
    university = models.CharField(max_length=200, default = "IPU")



    def __str__(self):
        return self.name

    class Meta:
        db_table = "collegs"
        verbose_name="College Table"
