from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *

# Register your models here.
# Customizes how admin panel shows data
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_staff', 'is_manager', 'is_employer')
    search_field = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)