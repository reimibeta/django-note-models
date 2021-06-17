from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django_datetime.date_time import datetime


class Note(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    is_edit = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.dnow())
    updated_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.created_date)


#
#
# @receiver(post_save, sender=Note)
# def add(sender, instance, created, **kwargs):
#     if created:
#         pass
#
#
@receiver(pre_save, sender=Note)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        if instance.updated_date is None:
            instance.updated_date = DateTime.datenow()

        old_value = Note.objects.get(id=instance.id)
        if old_value and old_value.text != instance.text:
            instance.is_edit = True

# @receiver(pre_delete, sender=Note)
# def delete(sender, instance, using, **kwargs):
#     pass
