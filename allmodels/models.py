from django.db import models

# Create your models here.

# to check all the fields present in the model
class AllFields(models.Model):
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    # removed
    # null_boolean_field = models.NullBooleanField()
    date_field = models.DateField()
    time_field = models.TimeField()
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    decimal_field = models.DecimalField(decimal_places=5,max_digits=9)
    float_field = models.FloatField()
    integer_field = models.IntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    small_integer_field = models.SmallIntegerField()
    char_field =models.CharField(max_length=20)
    text_field = models.TextField()
    # removed
    # comma_separated_integer = models.CommaSeparatedIntegerField(max_length=50)
    email_field =models.EmailField()
    file_field = models.FileField()
    #filepath_field = models.FilePathField()
    image_field = models.ImageField()
    generic_ip_address_field = models.GenericIPAddressField()
    slug_field = models.SlugField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()

class Student(models.Model):
    choices = (
        ('f','female'),
        ('m', 'male'),
        ('u','undisclosed')
    )
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=10)
    phone_no =models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()
    gender = models.CharField(choices=choices , max_length=1 ,default="Please Enter Gender")



















