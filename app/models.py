from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Bookmark(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    link = models.CharField(max_length=250)
    collector = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='bookmarks')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:bookmark_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
