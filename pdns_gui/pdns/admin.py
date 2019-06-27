from django import forms as django_forms
from django.contrib import admin
from django.db import models as django_models
from django.urls import reverse
from django.utils.safestring import mark_safe

from django_admin_relation_links import AdminChangeLinksMixin

from urllib.parse import urlencode

from . import inlines, models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CryptoKey)
class CryptoKeyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Domain)
# class DomainAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
class DomainAdmin(admin.ModelAdmin):
    list_display = ["name", "domain_type", "records"]

    readonly_fields = ["records"]

    ordering = ["name"]

    search_fields = ["name"]

    @staticmethod
    def records(obj):
        return mark_safe(
            '<a href="{}?{}" class="changelink"></a>'.format(
                reverse("admin:pdns_record_changelist"),
                urlencode({"domain__id__exact": obj.id}),
            )
        )


@admin.register(models.DomainMetadata)
class DomainMetadataAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["name", "rrtype", "prio", "content"]

    search_fields = ["name", "content"]
    list_filter = ["rrtype", "domain"]

    # ordering = ["name"]

    formfield_overrides = {
        django_models.TextField: {
            "widget": django_forms.TextInput(attrs={"size": "40"})
        }
    }


@admin.register(models.Supermaster)
class SupermasterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TsigKey)
class TsigKeyAdmin(admin.ModelAdmin):
    pass
