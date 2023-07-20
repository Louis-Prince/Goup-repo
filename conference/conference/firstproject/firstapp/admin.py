from django.contrib import admin
from .models import conference,Speaker_management,Schedule_management
# Register your models here.
admin.site.register(conference)
admin.site.register(Speaker_management)
admin.site.register(Schedule_management)