from django.contrib import admin
from .models import User, Post

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("usersFollowed",)

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ("usersLiked",)
    readonly_fields = ('timestamp',)

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)