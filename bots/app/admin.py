from django.contrib import admin

from app.models import Robot


# Register your models here.
class RobotAdmin(admin.ModelAdmin):
    list_display = ("name", 'description','created_at')
    search_fields = 'name',
    list_filter = 'name',


admin.site.register(Robot, RobotAdmin)
