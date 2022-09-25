
from django.db import models


class Montact(models.Model):
    Chat = models.CharField(max_length=200, default="null")
    Intent = models.CharField(max_length=200, default="null")
    Sender_ID = models.CharField(max_length=200, default='10000')

    def __str__(self):
        return self.Intent

class Contact(models.Model):
    Utterance = models.CharField(max_length=200, default="null")
    Entities = models.CharField(max_length=500, default="null")
    Traits = models.CharField(max_length=500, default="null")
    Shrug = models.ForeignKey(Montact, null=True, on_delete=models.SET_NULL)
    Details = models.JSONField()











