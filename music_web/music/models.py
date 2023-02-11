from django.db import models

# Create your models here.
class VideoYT(models.Model):
    video_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.SlugField(max_length=150)
    photo = models.ImageField(blank=True)


class PlayListYT(models.Model):
    photo = models.ImageField(blank=True)
    url = models.SlugField(max_length=150)
    title = models.CharField(max_length=100, blank=True)


class VideoPlayList(models.Model):
    video = models.ForeignKey("VideoYT", on_delete=models.CASCADE)
    playlist = models.ForeignKey("PlayListYT", on_delete=models.CASCADE)