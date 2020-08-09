from django.db import models

# Create your models here.
class UploadData(models.Model):
    """
    Model to store uploaded data to a location MEDIA_ROOT/uploads/ folder
    """
    upload = models.FileField(upload_to='uploads/')




