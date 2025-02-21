from django.conf import settings
from django.db import models
from django.utils import timezone

class FashionPiece(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Keeps track of the user who submitted
    piece_name = models.CharField(max_length=200)  # Title of the design
    description = models.TextField()  # Description of the piece
    image = models.ImageField(upload_to='fashion_pieces/')  # You can upload an image of the piece
    created_date = models.DateTimeField(default=timezone.now)  # Keep this for tracking
    published_date = models.DateTimeField(blank=True, null=True)  # Optional, if you want to track when it's shown on the site

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.piece_name
