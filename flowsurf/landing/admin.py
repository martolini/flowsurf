from django.contrib import admin
from .models import Subscriber



class SubAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone')

admin.site.register(Subscriber, SubAdmin)
