from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Accion

# Register your models here.
admin.site.unregister(Group)

class AccionesInline(admin.StackedInline):
    model = Accion

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [AccionesInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

