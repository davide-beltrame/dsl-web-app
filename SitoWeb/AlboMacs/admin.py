from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Achievement)
admin.site.register(models.Person)
admin.site.register(models.New)
admin.site.register(models.Course)