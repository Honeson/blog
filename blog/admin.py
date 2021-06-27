from django.contrib import admin

from .models import Post, Comment, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'slug']
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'publish', 'status']
    list_filter = ['status', 'publish']
    search_fields = ['name', 'email', 'content']


admin.site.register(Category)
