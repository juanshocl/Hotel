from django.db import models

import uuid

class Contact(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(default = None, max_length=50, blank=True)
    LastName = models.CharField(default = None, max_length=50, blank=True)
    Email = models.CharField(default = None, max_length=50, blank=True)
    Message = models.CharField(default = None, max_length=50, blank=True)
    DateMessage = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.Email
