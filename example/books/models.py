import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from imagekit import ImageSpec
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust, ResizeToFit
from .processors import Watermark_opacity, Watermark, WatermarkText


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = ProcessedImageField(
        verbose_name=('cover'),
        upload_to='covers/',
        #width_field='width',
        #height_field='height',
        blank=True,
        processors=[
            ResizeToFit(400, 600,
                        # upscale=False
                        ),
            Watermark_opacity(),
        ],
        format='JPEG',
        #options={'quality': 90},
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
