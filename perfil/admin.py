from django.contrib import admin

from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title','description',)
    list_filter = ('created','updated',)
    search_fields = ('title','description',)
    readonly_fields = ('created','updated',)
