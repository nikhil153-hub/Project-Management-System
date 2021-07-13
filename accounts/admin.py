from django.contrib import admin
from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    readonly_fields = ('password', )


admin.site.register(User, UserAdmin)
