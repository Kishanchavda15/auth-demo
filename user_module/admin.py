from django.contrib import admin

from user_module.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "is_active", "is_superuser", "is_staff",]