# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomingTransaction',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('tx', models.BinaryField()),
                ('tx_name', models.CharField(db_index=True, max_length=64)),
                ('tx_pk', models.UUIDField(db_index=True)),
                ('producer', models.CharField(db_index=True, help_text='Producer name', max_length=200)),
                ('action', models.CharField(choices=[('I', 'Insert'), ('U', 'Update'), ('D', 'Delete')], max_length=1)),
                ('timestamp', models.CharField(db_index=True, max_length=50)),
                ('consumed_datetime', models.DateTimeField(blank=True, null=True)),
                ('consumer', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('is_ignored', models.BooleanField(db_index=True, default=False, help_text='Ignore if update')),
                ('is_error', models.BooleanField(db_index=True, default=False)),
                ('error', models.TextField(blank=True, max_length=1000, null=True)),
                ('batch_seq', models.IntegerField(blank=True, null=True)),
                ('batch_id', models.IntegerField(blank=True, null=True)),
                ('is_consumed', models.BooleanField(db_index=True, default=False)),
                ('is_self', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'ordering': ['timestamp', 'producer'],
            },
        ),
        migrations.CreateModel(
            name='OutgoingTransaction',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('tx', models.BinaryField()),
                ('tx_name', models.CharField(db_index=True, max_length=64)),
                ('tx_pk', models.UUIDField(db_index=True)),
                ('producer', models.CharField(db_index=True, help_text='Producer name', max_length=200)),
                ('action', models.CharField(choices=[('I', 'Insert'), ('U', 'Update'), ('D', 'Delete')], max_length=1)),
                ('timestamp', models.CharField(db_index=True, max_length=50)),
                ('consumed_datetime', models.DateTimeField(blank=True, null=True)),
                ('consumer', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('is_ignored', models.BooleanField(db_index=True, default=False, help_text='Ignore if update')),
                ('is_error', models.BooleanField(db_index=True, default=False)),
                ('error', models.TextField(blank=True, max_length=1000, null=True)),
                ('batch_seq', models.IntegerField(blank=True, null=True)),
                ('batch_id', models.IntegerField(blank=True, null=True)),
                ('is_consumed_middleman', models.BooleanField(db_index=True, default=False)),
                ('is_consumed_server', models.BooleanField(db_index=True, default=False)),
                ('using', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
