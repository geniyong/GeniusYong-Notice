from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from apps.crawl.models import Info


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pid', 'content', 'site_name', 'site_url', 'post_created_at', 'created_at', 'edited_at']
