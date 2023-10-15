# pokemon/models.py
from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    ability = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/img/')
    evolution = models.CharField(max_length=100, blank=True, null=True)  # 여기서 수정

    def __str__(self):
        return self.name
