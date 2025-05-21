from django.contrib import admin
from .models import MyModel, Posts, Comment,VerifiedBadge
# Register your models here.

class PostsInline(admin.TabularInline):
    model = Posts
    extra = 1

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    inlines = [PostsInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment')
    filter_horizontal = ('post',)

class VerifiedBadgeAdmin(admin.ModelAdmin):
    list_display=('badge','issued_date', 'valid_until')

admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(VerifiedBadge, VerifiedBadgeAdmin)

