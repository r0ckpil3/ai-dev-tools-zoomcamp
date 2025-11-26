from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "completed", "priority", "due_date", "created_at", "updated_at")
    list_filter = ("completed", "priority", "due_date")
    search_fields = ("title", "description", "owner__username")