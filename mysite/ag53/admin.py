from django.contrib import admin
from ag53.models import User,Age,Branch,Gender,Email,Password

class email_inline(admin.StackedInline):
    model = Email
    extra = 1

class password_inline(admin.StackedInline):
    model = Password
    extra = 1
    max_value = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [email_inline,password_inline]

admin.site.register(User,UserAdmin)
admin.site.register(Age)
admin.site.register(Branch)
admin.site.register(Gender)
admin.site.register(Email)
