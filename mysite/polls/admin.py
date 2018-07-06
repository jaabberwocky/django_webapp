from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# this registers Question model to the admin view, making it editable!
admin.site.register([Question, Choice])