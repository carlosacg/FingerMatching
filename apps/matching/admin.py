from django.contrib import admin
from apps.matching.models import AlbumImage
# Register your models here.
@admin.register(AlbumImage)
class AlbumImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
