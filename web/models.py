from django.db import models

# Create your models here.
class wicha(models.Model):
    subject_id = models.CharField(max_length=30)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.id},{self.name}'