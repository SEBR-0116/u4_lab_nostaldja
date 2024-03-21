from django.contrib import admin

# Register your models here.
from .models import Century, Decade, Fad
admin.site.register(Century)
admin.site.register(Decade)
admin.site.register(Fad)