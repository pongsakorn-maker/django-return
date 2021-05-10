from django.db import models
from artist.models import Artist

class Single(models.Model):
    artist = models.ForeignKey(Artist,to_field='id',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    youtube_views = models.IntegerField()

    class Meta:
        db_table = 'single'