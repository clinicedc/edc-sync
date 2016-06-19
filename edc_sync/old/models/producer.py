from django.db import models

from edc_base.model.models import BaseUuidModel

from .password_field import PasswordModelField
from .sync_model_mixin import SyncModelMixin


class ProducerManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Producer(SyncModelMixin, BaseUuidModel):

    name = models.CharField(
        max_length=200,
        help_text='Usually hostname-database_name. e.g mpp83-bhp041_survey',
        unique=True)

    settings_key = models.CharField(
        max_length=200,
        help_text='Key in settings.DATABASES, usually hostname of producer',
        unique=True)

    url = models.CharField(max_length=64)

    db_host = models.CharField(
        verbose_name="Producer host name.",
        max_length=200,
        null=True,
        blank=True,
        help_text=("provide the IP address / hostname of the producer."))

    db_user = models.CharField(
        verbose_name="Database username in Django settings.",
        max_length=25,
        default='root',
        null=True,
        help_text=("provide the database username of the producer."))

    db_name = models.CharField(
        verbose_name="Database name in Django settings.",
        max_length=25,
        null=True,
        help_text=("provide the database name of the producer."))

    port = models.CharField(
        verbose_name="Database port.",
        max_length=25,
        default='',
        blank=True,
        null=True,
        help_text=("provide the database name of the producer."))

    db_password = PasswordModelField(
        verbose_name="Database password.",
        max_length=213,
        null=True,
        help_text=("provide the password to database on the producer."))

    is_active = models.BooleanField(
        default=True)

    sync_datetime = models.DateTimeField(
        null=True)

    sync_status = models.CharField(
        max_length=250,
        default='-',
        null=True)

    json_limit = models.IntegerField(
        default=0)

    json_total_count = models.IntegerField(
        default=0)

    comment = models.TextField(
        max_length=50,
        null=True,
        blank=True)

    objects = ProducerManager()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return (self.name, )

    class Meta:
        app_label = 'edc_sync'
        ordering = ['name']
        unique_together = (('settings_key', 'is_active'), )