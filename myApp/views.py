from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'First room'},
#     {'id': 2, 'name': 'Second room'},
#     {'id': 3, 'name': 'Third room'},
# ]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'room.html', context)