from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.Record, dispatch_uid="update_soa")
def update_soa(sender, instance, **kwargs):
    soa = models.Record.objects.get(domain=instance.domain, rrtype="SOA")
    print(soa)
    print(kwargs)
