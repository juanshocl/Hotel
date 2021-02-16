from django.db import models
import uuid

class UserProfile(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Rut = models.CharField(max_length=50, default=None)
    Name =  models.CharField(max_length=50, default=None)
    LastName =  models.CharField(max_length=50, default=None)
    Address =  models.CharField(max_length=50, default=None)
    Email =   models.CharField(max_length=50, default=None)

    def __str__(self):
        return (self.Name +' '+self.LastName)