from django.contrib import admin
from .models import Bus_stand, Buses, Passenger

# Register your models here.

admin.site.register(Buses)
admin.site.register(Bus_stand)
admin.site.register(Passenger)
