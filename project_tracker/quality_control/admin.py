from django.contrib import admin
from .models import BugReport, FeatureRequest


# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'created_at', 'updated_at')
    list_filter = ('title', 'status', 'project')
    search_fields = ('title', 'project')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'project')
        }),
    )

    actions = ['mark_as_fixed']

    def mark_as_fixed(self, request, queryset):
        queryset.update(status='Fixed')


# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('title', 'status', 'project')
    search_fields = ('title', 'project')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'project', 'priority')
        }),
    )

