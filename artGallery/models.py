from django.db import models
from django.urls import reverse

# Create your models here.
class Art(models.Model):
    artist_name = models.CharField(max_length=200)
    name_of_art = models.CharField(max_length=200)
    up_for_sale = models.BooleanField()
    estimated_evaluation = models.FloatField()
    image_of_art = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name_of_art

    def get_absolute_url(self):
        return reverse("artGallery:detail", kwargs={"pk": self.pk})
