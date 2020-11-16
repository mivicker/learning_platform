from django.contrib.admin import ModelAdmin, register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Team

@register(User)
class UserAdmin(BaseUserAdmin):
	model = User

	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Team', {'fields': ('team', 'role', 'buddy')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
		(('Permissions'), {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'team', 'role', 'password1', 'password2'),
        }),
    )

@register(Team)
class TeamAdmin(ModelAdmin):
	model = Team