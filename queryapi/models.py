from django.db import models

class Student(models.Model):
    roll = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name} with roll no. {self.roll}'


