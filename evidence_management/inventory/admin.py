from django.contrib import admin

# Register your models here.
from . models import Case, Evidence

admin.site.register(Case)
admin.site.register(Evidence)