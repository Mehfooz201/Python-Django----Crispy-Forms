from django.contrib import admin
from .models import myForm

# Register your models here.

@admin.register(myForm)
class FormsAdmin(admin.ModelAdmin):
    list_display= ['form_id', 'uname', 'title', 'description']