from django.contrib import admin
from .models import zoom

class ZoomModelAdmin(admin.ModelAdmin):
    model = zoom
    list_display = ["user", "conferma", "casa"]
# Register your models here.
admin.site.register(zoom, ZoomModelAdmin)
