from django.db import models
from django.utils import timezone


# Create your models here.
# =======================================================================================================
# Purpose : This has been used to create the table "urlapp_shrterurl" after migration
# Attributes : short_url : hashed data after MD5 encoding
#              original_url : original url which has to be shortened
#              created_at : Record creation timestamp
#              expired_at : expiry timestamp for short url
#              active : status of the short url whether it is active or not
# =======================================================================================================
class ShorterUrl(models.Model):
    short_url = models.CharField(max_length=50)
    original_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now())
    expired_at = models.DateTimeField()
    active = models.BooleanField(default=True)
