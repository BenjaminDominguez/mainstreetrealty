from django.contrib import admin
from .models import Property, Status, NewLead
from django import forms


admin.site.register(Property)
admin.site.register(Status)
admin.site.register(NewLead)
