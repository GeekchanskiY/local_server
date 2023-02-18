from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'is_staff', 'is_active', 'is_superuser',)
    list_display = ('username', 'is_superuser')
    list_filter = ('is_superuser', )
    search_fields = ('username', )
