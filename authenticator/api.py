import io
from authenticator.schemas import IdentitySchema, PostFace, PostItem
import json
from typing import List
from django.forms import ImageField
from ninja import NinjaAPI
import qrcode
import qrcode.image
from django.shortcuts import get_object_or_404
from requests import post
#from django.db.models import Product
from authenticator.models import Process, Identity, Face
import base64
from io import BytesIO
from PIL import Image
import uuid
from urllib.request import Request
import base64
from django.core.files.images import ImageFile 
import face_recognition
import cv2
api = NinjaAPI()


'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''
#sorun yok,

@api.get("/process")
def process(request):
    data = Process.objects.create()
    img = qrcode.make(data.id)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    image = io.BytesIO(buffered.getvalue())
    qr = Process(qrcode=ImageFile(image, name=f"{str(data)}.jpg"))
    qr.save()
    return 200, {"qr": buffered.getvalue(), "process_id": data.id,"time":data.started_at }

@api.get("/process/{process_id}")
def get_process(request, process_id: uuid.UUID):
    proc = get_object_or_404(Process, id=process_id)
    return {"process_id": proc.id, "avg_distance" : proc.avg_distance }

@api.post("/process/{process_id}/identity")
def save_identity(request, process_id:uuid.UUID, posted: IdentitySchema):
    identity = Identity.objects.create(process_id=Process.objects.get(id=process_id),
    documentType = posted.documentType,country = posted.country,surnames = posted.surnames, givenNames = posted.givenNames,
    documentNumber = posted.documentNumber,nationalityCode = posted.nationalityCode,birthdate = posted.birthdate,sex = posted.sex,
    expiryDate = posted.expiryDate, personalNumber = posted.personalNumber,personalNumber2 = posted.personalNumber2, bio_image = posted.bio_image)






    image = io.BytesIO(base64.b64decode(posted.bio_image))

    identity = Identity(process_id=Process.objects.get(id=process_id), documentType = posted.documentType, country= posted.country,
     givenNames = posted.givenNames, surnames=posted.surnames, documentNumber = posted.documentNumber, nationalityCode = posted.nationalityCode,
     birthdate = posted.birthdate, sex = posted.sex, expiryDate = posted.expiryDate, personalNumber= posted.personalNumber, 
     personalNumber2 = posted.personalNumber2, bio_image=ImageFile(image, name=f"{str(uuid.uuid4())}.jpg"))

    identity.save()

    return {'personal number' :posted.personalNumber}

@api.post("/process/{process_id}/face")
def save_face(request, process_id: uuid.UUID,  post_face: PostFace):

    image = io.BytesIO(base64.b64decode(post_face.face))

    face = Face(process_id=Process.objects.get(id=process_id), face=ImageFile(image, name=f"{str(uuid.uuid4())}.jpg"))
    face.save()


    known_image = face_recognition.load_image_file("media/bio/derda.jpg")
    known_face_locations = face_recognition.face_locations(known_image)
    known_face_encodings = face_recognition.face_encodings(known_image, known_face_locations)

    
    unknown_image = cv2.imread(face.face.path)
    unknown_image = cv2.resize(unknown_image, (0, 0), fx=0.25, fy=0.25)
    unknown_face_locations = face_recognition.face_locations(unknown_image)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image, unknown_face_locations)
    print(len(known_face_encodings))
    print(len(unknown_face_encodings))

    # known_image = face_recognition.load_image_file("media/bio/derda.jpg")
    # unknown_image = face_recognition.load_image_file(face.face.path)
    # print(len(face_recognition.face_encodings(unknown_image)))
    # biden_encoding = face_recognition.face_encodings(known_image)[0]
    # unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    result = face_recognition.face_distance([unknown_face_encodings[0]], known_face_encodings[0])[0].item()

    face.distance = result
    face.save()
    
    avg = Process.objects.get(id=process_id)
    strAvg = str(avg.avg_distance)
    
    return {"distance": face.distance}

@api.post("/post")
def save_sil(request: Request, post_item: PostItem):
    return {"face1": post_item.key1}



