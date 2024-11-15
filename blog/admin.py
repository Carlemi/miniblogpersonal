from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'title', 'description', 'created')
    list_display_links = ('id', 'title',)
    list_filter = ('created','updated',)
    search_fields = ('title', 'description')
    readonly_fields = ('created','updated',)