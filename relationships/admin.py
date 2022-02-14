from django.contrib import admin

from relationships.models import Article, Author

# Register your models here.
admin.site.register([
    Article,
    Author
])