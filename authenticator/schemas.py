from datetime import date
from ninja import Schema

class IdentitySchema(Schema):
    documentType: str
    country: str
    surnames: str
    givenNames:str
    documentNumber: str
    nationalityCode: str
    birthdate: str
    sex: str
    expiryDate: str
    personalNumber: str
    personalNumber2: str
    bio_image: str
    
class PostItem(Schema):
    key1: str

class PostFace(Schema):
    face: str
