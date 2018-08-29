from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date') 

admin.site.register(Project, ProjectAdmin)

