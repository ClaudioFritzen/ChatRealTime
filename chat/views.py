from django.shortcuts import render, redirect,get_list_or_404

from django.http import HttpResponse, HttpResponseRedirect

from chat.models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkviews(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')

        # Verifique se a sala já existe no banco de dados
        room_exists = Room.objects.filter(name=room_name).exists()

        if room_exists:
            # Se a sala existir, redirecione para a página do bate-papo
            return redirect(f'/{room_name}/?username={username}')
        else:
            # Se a sala não existir, crie uma sala de bate-papo
            new_room = Room.objects.create(name=room_name)
            new_room.save()  # Salve a nova sala no banco
            return redirect(f'/{room_name}/?username={username}')
    
    return HttpResponse('Requisição inválida')
