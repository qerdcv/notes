import asyncio
import json
import logging

from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from datetime import datetime

from .models import Notes


logger = logging.getLogger(__name__)


class NotesConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        self.user = f'{self.scope["user"]}'
        logger.info(f'{self.user} connect to the websocket')
        await self.channel_layer.group_add(
            self.user,
            self.channel_name
        )

        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        data = json.loads(event.get('text'))
        response_data = {}
        if data.get('type') == 'add':
            obj_id = await self.save_note(self.scope['user'], data.get('text'))
            logger.info(f'{self.user} add note to database (note_id:{obj_id})')
            response_data.update({"type": "add",
                                  "text": data.get("text"),
                                  "id": obj_id})
        elif data.get('type') == 'change_status':
            await self.change_status(data.get("id"), data.get("status"))
            logger.info(f'{self.user} status of note to {data.get("status")} (note_id:{data.get("id")})')
            response_data.update({"type": "change_status",
                                  'id': data.get('id'),
                                  'status': data.get('status')})
        await self.channel_layer.group_send(
            self.user,
            {
                "type": "note",
                "text": json.dumps(response_data)
            }
        )

    async def note(self, event):
        await self.send(
            {
                "type": "websocket.send",
                "text": event['text']
            }
        )

    @database_sync_to_async
    def save_note(self, user, note_text):
        obj = Notes.objects.create(user=get_user_model().objects.get(id=user.id), note=note_text)
        obj.save()
        return obj.id

    @database_sync_to_async
    def change_status(self, pk, status):
        obj = Notes.objects.get(id=pk)
        obj.is_done = status
        obj.save()

    async def websocket_disconnect(self, event):
        logger.info(f'{self.user} disconnect to the websocket')
