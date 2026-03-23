from django.contrib import admin

# Register your models here.
from .models import Post, PostIntroduction

class PostAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update',
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(PostIntroduction)
