from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import now

from djangoql.queryset import DjangoQLQuerySet


class Book(models.Model):
    name = models.CharField(max_length=10)  # lol, we're minimalists
    author = models.ForeignKey('auth.User')
    written = models.DateTimeField(default=now)
    is_published = models.BooleanField(default=False)
    rating = models.FloatField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = DjangoQLQuerySet.as_manager()
