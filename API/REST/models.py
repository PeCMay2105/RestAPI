from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.titulo



