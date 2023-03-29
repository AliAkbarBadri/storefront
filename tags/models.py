from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Generic relationship
    # Type of an object (product, video, article etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID: assume pk is an intger (th limitaion of the solution)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
