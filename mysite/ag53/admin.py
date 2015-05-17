from django.contrib import admin
from ag53.models import Profile,Age,Branch,Gender,Email
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class email_inline(admin.StackedInline):
    model = Email
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [email_inline]




class profile_inline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (profile_inline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Age)
admin.site.register(Branch)
admin.site.register(Gender)
admin.site.register(Email)
