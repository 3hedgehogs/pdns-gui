from django import forms
from django.db import models as django_models

from .. import admin

from . import models


class RecordInline(admin.TabularInline):
    model = models.Record

    fields = ["name", "rrtype", "prio", "content"]
    readonly_fields = ["name", "rrtype"]

    ordering = ["name"]

    extra = 0

    formfield_overrides = {
        django_models.TextField: {"widget": forms.TextInput(attrs={"size": "50"})}
    }
