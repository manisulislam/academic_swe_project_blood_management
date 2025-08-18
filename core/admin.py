from django.contrib import admin
from .models import Announcement , ContactMessage

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'is_urgent', 'expiry_date')
    list_filter = ('is_urgent', 'created_on', 'expiry_date')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created_on'
    ordering = ('-created_on',)



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_on',)
    ordering = ('-created_on',)