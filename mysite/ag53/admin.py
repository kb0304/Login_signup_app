from django.contrib import admin
from ag53.models import Profile,Age,Branch,Gender,Email

class email_inline(admin.StackedInline):
    model = Email
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [email_inline]

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Age)
admin.site.register(Branch)
admin.site.register(Gender)
admin.site.register(Email)
