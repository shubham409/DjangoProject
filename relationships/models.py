
from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator 

from django.core.exceptions import ValidationError
# Create your models here.

# Types of relation ship 
# 1. Many to one (many articles can be mapped with single author )
# on cascade means when we delete author articles will also be deleted
class Article(models.Model) :
    title =  models.CharField( max_length=100 ,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(100)
        ]
    )
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} with author {self.author}"

class Author(models.Model) :
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(50)
        ]
    )

    def __str__(self) -> str:
        return f"{self.name} with id {self.pid}"

# querries 
# """ 
# 
# """

# many to many 
class Person(models.Model):
    person_name = models.CharField(max_length=50)
    society = models.ManyToManyField('Society')
    def __str__(self) -> str:
        return self.person_name

class Society(models.Model):
    society_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.society_name



