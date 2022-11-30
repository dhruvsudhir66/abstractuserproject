from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm,UserAdminCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'admin']
    list_filter = ['admin','staff','active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password','password_2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)