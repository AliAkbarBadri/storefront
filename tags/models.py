from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TaggedItemManager(models.Manager):
    # get_tags_for(Product, 1)
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects.select_related("tag").filter(
            content_type=content_type,  # id of store product in django_content_type table
            object_id=obj_id,  # target product_id
        )


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    # what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Generic relationship
    # Type of an object (product, video, article etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID: assume pk is an intger (th limitaion of the solution)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
