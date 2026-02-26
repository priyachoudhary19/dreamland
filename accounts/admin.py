from django.contrib import admin
from .models import Author, registration
# Register your models here.

admin.site.register(Author)

class registrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'address')
admin.site.register(registration, registrationAdmin)