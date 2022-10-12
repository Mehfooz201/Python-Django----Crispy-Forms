from django.db import models

# Create your models here.

class myForm(models.Model):
    form_id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.TextField()
