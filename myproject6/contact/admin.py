from django.contrib import admin
from contact.models import ContactMessage
# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')
    list_filter = ('name', 'email', 'timestamp')
    search_fields = ('name', 'email')
    ordering = ('name',)
