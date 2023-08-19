from django.shortcuts import render, redirect

from chat.models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkviews(resquest):

    room = resquest.POST['room_name']
    username = resquest.POST['username']

    # pesquisa no banco

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+new_room+'/?username='+username)