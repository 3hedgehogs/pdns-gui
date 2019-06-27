from django.contrib import admin


class InlineMixin:
    def get_readonly_fields(self, request, obj=None):
        if obj and hasattr(self, "changeonly_fields"):
            changeonly_fields = getattr(self, "changeonly_fields", [])
            fields = self.get_fields(request, obj)
            return [field for field in fields if field not in changeonly_fields]

        return self.readonly_fields


class TabularInline(InlineMixin, admin.TabularInline):
    def get_max_num(self, request, obj=None, **kwargs):
        if not self.has_change_permission(request):
            return 0

        return getattr(self, "max_num", None)
