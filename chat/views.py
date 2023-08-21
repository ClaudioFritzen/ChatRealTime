from django.shortcuts import render, redirect, HttpResponse

from chat.models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkviews(resquest):

    room = resquest.POST.get('room_name')
    username = resquest.POST.get('username')
    print(room)
    print(username)
    # pesquisa no banco

    room = Room.objects.filter(name=room).exists()

    if room:
        return HttpResponse('Cheguei aqui!!')
        #return redirect('/'+room+'/?username'+username)

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return HttpResponse('Else')
        #return redirect('/'+room+'/?username'+username) 