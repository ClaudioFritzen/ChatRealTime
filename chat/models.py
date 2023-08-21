from django.db import models
from datetime import datetime
from django.contrib.auth.models import User  # Importe a classe User se ainda não tiver feito isso

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que enviou a mensagem
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Sala à qual a mensagem pertence
