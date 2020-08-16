from django.db import models
from django.contrib import admin
from .models import Project
from markdownx.admin import MarkdownxModelAdmin

# Register your models here
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectName', 'version', 'pub_date')
    list_filter = ('projectName', 'pub_date')
    search_fields = ('projectName', 'version')

admin.site.register(Project, ProjectAdmin)
