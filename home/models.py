# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user_type = models.CharField(max_length=255, null=True, blank=True)
    otp = models.CharField(max_length=255, null=True, blank=True)
    otp_expires = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Applicant(models.Model):

    #__Applicant_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    first_names = models.CharField(max_length=255, null=True, blank=True)
    initials = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    id_type = models.CharField(max_length=255, null=True, blank=True)
    id_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user_id = models.CharField(max_length=255, null=True, blank=True)

    #__Applicant_FIELDS__END

    class Meta:
        verbose_name        = _("Applicant")
        verbose_name_plural = _("Applicant")


class Application(models.Model):

    #__Application_FIELDS__
    appliant_id = models.IntegerField(null=True, blank=True)
    application_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    application_step = models.CharField(max_length=255, null=True, blank=True)
    application_status = models.CharField(max_length=255, null=True, blank=True)

    #__Application_FIELDS__END

    class Meta:
        verbose_name        = _("Application")
        verbose_name_plural = _("Application")


class Document(models.Model):

    #__Document_FIELDS__
    applicant_id = models.IntegerField(null=True, blank=True)
    document_type = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    document_status = models.CharField(max_length=255, null=True, blank=True)
    status_date = models.CharField(max_length=255, null=True, blank=True)
    last_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified_by = models.IntegerField(null=True, blank=True)

    #__Document_FIELDS__END

    class Meta:
        verbose_name        = _("Document")
        verbose_name_plural = _("Document")


class Request(models.Model):

    #__Request_FIELDS__
    user_name = models.CharField(max_length=255, null=True, blank=True)
    applicant_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    last_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified_by = models.IntegerField(null=True, blank=True)

    #__Request_FIELDS__END

    class Meta:
        verbose_name        = _("Request")
        verbose_name_plural = _("Request")



#__MODELS__END
