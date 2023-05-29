from django.db import models

# Create your models here.


class QRCode(models.Model):
    image = models.ImageField(upload_to='qr_codes/')
