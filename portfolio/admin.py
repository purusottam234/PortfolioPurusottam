from .models import Contact
from django.contrib import admin
from .models import Project

admin.site.register(Project)
admin.site.register(Contact)
