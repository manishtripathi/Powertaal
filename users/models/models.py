from django.db import models

# Create your models here.
class FreeUser(models.Model):
    FreeUserId = models.BigAutoField(primary_key=True)
    UserName = models.CharField(max_length=255)
    Place = models.CharField(max_length=255, blank=True, null=True)
    CreatedDate = models.DateTimeField()
    CreatedBySource = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblFreeUser'