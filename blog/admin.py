from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'short_description', 'created_at', 'updated_at')
    fieldsets = [
        ('Information',
         {
             'fields': ['title', 'short_description']
         }),
        (None, {
            'fields': ['content']
        })
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
