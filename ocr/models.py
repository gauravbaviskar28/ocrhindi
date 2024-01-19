from django.db import models
from django.db.models.base import Model
# Create your models here.


class ocrmodel(models.Model):
    img=models.ImageField(upload_to='images')
    desc=models.TextField(max_length=50000,blank=True)
    def __str__(self):
        return str(self.id)

class ocrmodelcoord(models.Model):
    ocrmodel1=models.ForeignKey(ocrmodel,on_delete=models.CASCADE)
    left=models.IntegerField()
    top=models.IntegerField()
    word=models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)