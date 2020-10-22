from django.db import models

# Create your models here.
class Queues(models.Model):
    name = models.CharField(max_length=255)
    max_vcore = models.CharField(max_length=255)


class QueueUseRate(models.Model):
    queue = models.ForeignKey(Queues, related_name='use_rate',on_delete=models.CASCADE)


