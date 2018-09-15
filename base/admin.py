from django.contrib import admin

from .models import SiteSetting


# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


@admin.register(SiteSetting)
class SiteSettingAdmin(BaseAdmin):
    fields = ('key', 'value')
    list_display = ('key', 'value')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        from django.core.cache import cache
        if cache.has_key('settings'):
            cache.delete('settings')
