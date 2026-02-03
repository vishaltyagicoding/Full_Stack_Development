from django.contrib import admin
from .models import Students

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'enrolled_date', 'city')
    list_filter = ('name', 'age', 'email', 'enrolled_date', 'city')
    search_fields = ('age', 'city')
    ordering = ('name',)




