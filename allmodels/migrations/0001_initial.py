# Generated by Django 4.0.2 on 2022-02-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllFields',
            fields=[
                ('binary_field', models.BinaryField()),
                ('boolean_field', models.BooleanField()),
                ('date_field', models.DateField()),
                ('time_field', models.TimeField()),
                ('date_time_field', models.DateTimeField()),
                ('duration_field', models.DurationField()),
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('big_integer_field', models.BigIntegerField()),
                ('decimal_field', models.DecimalField(decimal_places=5, max_digits=9)),
                ('float_field', models.FloatField()),
                ('integer_field', models.IntegerField()),
                ('positive_integer_field', models.PositiveIntegerField()),
                ('positive_small_integer_field', models.PositiveSmallIntegerField()),
                ('small_integer_field', models.SmallIntegerField()),
                ('char_field', models.CharField(max_length=20)),
                ('text_field', models.TextField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='')),
                ('filepath_field', models.FilePathField()),
                ('image_field', models.ImageField(upload_to='')),
                ('generic_ip_address_field', models.GenericIPAddressField()),
                ('slug_field', models.SlugField()),
                ('url_field', models.URLField()),
                ('uuid_field', models.UUIDField()),
            ],
        ),
    ]