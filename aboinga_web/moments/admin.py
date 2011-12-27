from django.contrib import admin
from moments.models import Moment

class MomentAdmin(admin.ModelAdmin):
    ordering = ["created_at"]
    search_fields = ['slug', 'photo']
    list_display = ['slug', 'photo', 'created_at', 'public']
admin.site.register(Moment, MomentAdmin)