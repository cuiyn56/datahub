from django.conf import settings
from django.db import models

'''
Datahub Models

@author: Anant Bhardwaj
@date: Mar 21, 2013
'''


class DataHubLegacyUser(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    f_name = models.CharField(max_length=50, null=True)
    l_name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    # `issuer` and `subject` are OIDC fields for identifying users based on
    # their identity provider and their uid at the provider. `max_length=255`
    # here is arbitrary.
    issuer = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = "datahub_legacy_users"


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    repo_base = models.CharField(max_length=50)
    repo_name = models.CharField(max_length=50)
    card_name = models.CharField(max_length=50)
    query = models.TextField()

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "cards"


class Annotation(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    url_path = models.CharField(max_length=500, unique=True)
    annotation_text = models.TextField()

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "annotations"


class App(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    app_id = models.CharField(max_length=100, unique=True)
    app_name = models.CharField(max_length=100)
    app_token = models.CharField(max_length=500)
    legacy_user = models.ForeignKey('DataHubLegacyUser', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    def __unicode__(self):
        return self.app_name

    class Meta:
        db_table = "apps"


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    legacy_user = models.ForeignKey('DataHubLegacyUser', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    app = models.ForeignKey('App')
    access = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "permissions"
