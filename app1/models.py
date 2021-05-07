from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FileUpload(models.Model):
    audio = models.FileField(blank=False, null=False)


#  # Message models
#
# account_sid = models.CharField(max_length=300, null=True, blank=True)
# api_version = models.CharField(max_length=300, null=True, blank=True)
# body = models.CharField(max_length=300, null=True, blank=True)
# date_created = models.CharField(max_length=300, null=True, blank=True)
# date_sent = models.CharField(max_length=300, null=True, blank=True)
# date_updated = models.CharField(max_length=300, null=True, blank=True)
# direction = models.CharField(max_length=300, null=True, blank=True)
# error_code = models.CharField(max_length=300, null=True, blank=True)
# error_message = models.CharField(max_length=300, null=True, blank=True)
# from = models.CharField(max_length=300, null=True, blank=True)
# messaging_service_sid = models.CharField(max_length=300, null=True, blank=True)
# num_media = models.CharField(max_length=300, null=True, blank=True)
# num_segments = models.CharField(max_length=300, null=True, blank=True)
# price = models.CharField(max_length=300, null=True, blank=True)
# price_unit = models.CharField(max_length=300, null=True, blank=True)
# sid = models.CharField(max_length=300, null=True, blank=True)
# status = models.CharField(max_length=300, null=True, blank=True)
# subresource_uris = models.CharField(max_length=300, null=True, blank=True)
# to = models.CharField(max_length=300, null=True, blank=True)
# uri = models.CharField(max_length=300, null=True, blank=True)