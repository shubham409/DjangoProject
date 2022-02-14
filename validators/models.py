from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator , MinLengthValidator
# Create your models here.
def age_validation(age):
    if age <14 :
        raise ValidationError('Age is too low ')
    elif age >100:
        raise ValidationError('Age is too high ')
    


class ValidationModel(models.Model):
    title  = models.CharField(max_length=50, validators=[
        MaxLengthValidator(50),
        MinLengthValidator(3)
    ])
    age = models.IntegerField(validators=[
        age_validation
    ])

    def __str__(self):
        return self.title








