from django.db import models
#importamos el timezone para poder agregarle valores a created y updated
from django.utils import timezone
#importamos utilidad para poder crear el primary key como uuid
import uuid

class ProfileInfo(models.Model):

    #Creamos una clase abstracta con las variables id, updated y created at
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(blank=True, null=True,editable=False)
    created_at = models.DateTimeField(blank=True,null=True,editable=False)

    #la definimos como abstracta
    class Meta:
        abstract = True

#nuestra segunda clase hereda de nuestra clase abstracta para que contenga las variables iniciales
class Profile(ProfileInfo):
    CHOICES = ((0, "Masculino"),(1,"Femenino"))
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    sex = models.IntegerField(choices=CHOICES)

    
    #Declaramos 3 metodos, uno para crear, uno para actualizar y otro para leer
    def create(self):
        self.created_at = timezone.now()
        self.save()
    
    def update(self):
        self.updated_at = timezone.now()
        self.save()
        
    def __str__(self):
        return self.name
