import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    context = {}
    return render(request, "chat/index.html", context)


def room(request, room_name):
    context = {
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    return render(request, 'chat/room.html', context)


