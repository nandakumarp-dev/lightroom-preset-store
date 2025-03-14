from django.db import models

class Preset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='preset_images/', default='preset_images/default.jpg')  # ✅ Allow blank images
    file = models.FileField(upload_to='preset_files/', help_text="Upload an .xmp file")

    def __str__(self):
        return self.name
