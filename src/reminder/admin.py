from django.contrib import admin

# Register your models here.
from .models import User, Notification

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'user_id', 'chat_id')
    list_display_links = ('user_id', 'id')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'order_number')
    list_display_links = ('id', 'order_number')
