from tkinter import CASCADE
from django.db import models

class Comment(models.Model):
    comment=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment