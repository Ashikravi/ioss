from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ShortenedURL

@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ['short_code', 'original_url', 'click_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['original_url', 'short_code']
    readonly_fields = ['short_code', 'created_at']