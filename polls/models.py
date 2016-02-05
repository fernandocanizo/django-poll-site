from django.db import models
from django.utils import timezone
from datetime import timedelta


class Poll(models.Model):
    text = models.CharField(max_length=200)
    created_ts = models.DateTimeField()
    updated_ts = models.DateTimeField(null=True, default=None)
    is_published = models.BooleanField(default=False)
    publication_date = models.DateTimeField(
        'date published',
        default=None,
        )

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.publication_date >= timezone.now() - timedelta(days=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_ts = timezone.now()
            self.updated_ts = timezone.now()
            return super(Poll, self).save(*args, **kwargs)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
