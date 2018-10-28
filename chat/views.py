import json

from django.shortcuts import render
from django.utils.safestring import mark_safe

from django.shortcuts import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import channels
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver


def index(request):
    room_name = 'chat'
    group_name = 'chat_chat'

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'chat_message',
            'message': "messagesssss"
        }
    )
    context = {}
    return render(request, "chat/index.html", context)


def room(request, room_name):
    context = {
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    return render(request, 'chat/room.html', context)
