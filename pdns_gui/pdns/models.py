from django.conf import settings
from django.db import models

import model_utils


class Comment(models.Model):
    domain = models.ForeignKey("Domain", models.DO_NOTHING)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    modified_at = models.IntegerField()
    account = models.CharField(max_length=40, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        db_table = "comments"


class CryptoKey(models.Model):
    domain = models.ForeignKey("Domain", models.DO_NOTHING)
    flags = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "cryptokeys"


class Domain(models.Model):
    name = models.CharField(unique=True, max_length=255)
    master = models.CharField(max_length=128, blank=True, null=True)
    last_check = models.IntegerField(blank=True, null=True)
    domain_type = models.CharField(max_length=6, db_column="type")
    notified_serial = models.PositiveIntegerField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = "domains"

    def update_soa(self):
        soa = Record.objects.get(domain=self, rrtype="SOA")
        print(soa)

    def __str__(self):
        return self.name


class DomainMetadata(models.Model):
    domain = models.ForeignKey("Domain", models.DO_NOTHING)
    kind = models.CharField(max_length=32, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "domainmetadata"

    def __str__(self):
        return self.domain


class Record(models.Model):
    domain = models.ForeignKey(
        "Domain", models.DO_NOTHING, blank=True, null=True, related_name="records"
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    rrtype = models.CharField(db_column="type", max_length=10, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True)
    prio = models.IntegerField(blank=True, null=True)
    disabled = models.BooleanField(blank=True, null=True)
    ordername = models.CharField(max_length=255, blank=True, null=True)
    auth = models.BooleanField(blank=True, null=True)
    # date_modified = models.DateTimeField(blank=True, null=True)

    tracker = model_utils.FieldTracker()

    class Meta:
        db_table = "records"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.rrtype not in settings.RRTYPES_WITH_PRIO:
            self.prio = None

        if self.tracker.changed():
            self.domain.update_soa()

        super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.domain.update_soa()

        super().delete(using, keep_parents)

    def __str__(self):
        fields = list(map(str, [self.name, self.rrtype, self.prio, self.content]))
        if self.rrtype not in settings.RRTYPES_WITH_PRIO:
            del fields[2]
        return " ".join(fields)


class Supermaster(models.Model):
    ip = models.CharField(primary_key=True, max_length=64)
    nameserver = models.CharField(max_length=255)
    account = models.CharField(max_length=40)

    class Meta:
        db_table = "supermasters"
        unique_together = (("ip", "nameserver"),)


class TsigKey(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    algorithm = models.CharField(max_length=50, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "tsigkeys"
        unique_together = (("name", "algorithm"),)


# def import_signals():
#     from . import signals  # noqa, pylint: disable=unused-import


# import_signals()
