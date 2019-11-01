from django.contrib import admin

# Register your models here.
from application_1.models import director, manager, engineer

admin.site.register(director)
admin.site.register(manager)
admin.site.register(engineer)
