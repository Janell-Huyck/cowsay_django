from django.db import models


class MooText(models.Model):
    text = models.TextField()
