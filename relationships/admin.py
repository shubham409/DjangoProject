from django.contrib import admin

from relationships.models import Article, Author, Person, Society

# Register your models here.
admin.site.register([
    Article,
    Author,

    Person,
    Society,
])