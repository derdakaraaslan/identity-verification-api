from asyncio.windows_events import NULL
from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
import datetime
# Create your models here.
class Process(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    started_at= models.DateTimeField(auto_now=True,null=False)
    finished_at=models.DateTimeField(auto_now=True,null=False)
    qrcode = models.ImageField(null = False, default = "no image", upload_to="qrcode")

    @property
    def avg_distance(self):
        total = 0
        for face in self.faces.all():
            total += face.distance
        return 1 if self.faces.count() == 0 else (total / self.faces.count())

    def __str__(self):
        return f"{self.id}"

class Identity(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    process_id=models.ForeignKey(Process, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now=True,null=False)
    documentType=models. CharField(null=False,max_length=10)
    country=models. CharField(null=False,max_length=40)
    givenNames=models. CharField(null=False,max_length=40)
    surnames=models. CharField(null=False,max_length=40)
    documentNumber=models. CharField(null=False,max_length=20)
    nationalityCode=models. CharField(null=False,max_length=20)
    birthdate=models. CharField(null=False,max_length=20)
    sex=models. CharField(null=False,max_length=10)
    expiryDate=models. CharField(null=False,max_length=20)
    personalNumber=models. CharField(null=False,max_length=20)
    personalNumber2=models. CharField(null=False,max_length=20)
    bio_image = models.ImageField(null=False, default="No image", upload_to ="bio")
    def __str__(self):
        return f"{self.process_id}"

class Face(models.Model):    
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    process_id = models.ForeignKey(Process, on_delete=models.CASCADE, related_name="faces")
    face = models.ImageField(upload_to="face")
    timestamp= models.DateTimeField(auto_now=True,null=False)
    distance = models.FloatField(default=1)
    def __str__(self):
        return f"{self.process_id}"