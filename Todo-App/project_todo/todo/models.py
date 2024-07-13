from django.db import models

# Create your models here.

class TodoModel(models.Model):
    task= models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.task

####problem when i enter empty task and saved it then this def __str__(self): return self.task gives me error while deleting such empty data