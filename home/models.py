from django.db import models

class Files(models.Model):
    file = models.FileField(upload_to='uploads/',blank='true')
    key=models.CharField(max_length=100,null=True,blank=True)