from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Order(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='imgorder/',
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'Order - {self.name}'

    class Meta:
        ordering = ['-timestamp', '-updated']


def create_slug(instance: Order, new_slug=None) -> str:
    slug = slugify(instance.name)

    if new_slug is not None:
        slug = new_slug
    qs = instance._meta.model.objects.filter(slug=slug).order_by('-id')
    duplicate_exist = qs.exists()
    if duplicate_exist:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_order_receiver(sender, instance: Order, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(receiver=pre_save_order_receiver, sender=Order)