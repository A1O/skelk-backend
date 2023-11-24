from django.contrib import admin
from .models import Post, Profile, Blog
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False


class UserProfileAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Post)
admin.site.register(Blog)
# admin.site.register(Profile)
