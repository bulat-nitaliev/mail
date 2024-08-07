import json
from djangochannelsrestframework.permissions import AllowAny
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)
from djangochannelsrestframework.observer import model_observer
from imap_tools import MailBox, AND
from .models import  Message, User
from general.api.serializers import MessageSerializer, UserListSerializer


class MessageConsumer(AsyncAPIConsumer):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny,]
    lookup_field = "pk"

    async def disconnect(self, code):
        await super().disconnect(code)

    
    @action()
    async def get_message(self, dic_mail, **kwargs):
        
        login = dic_mail['login']
        password = dic_mail['password']
        lst = []
        with MailBox('imap.yandex.ru').login(login, password) as mailbox:
            # print({{key: val} for i in mailbox.fetch() for key,val in i.items() })
            for msg in mailbox.fetch():
                data = {}
                data['dt'] = str(msg.date)
                data['subject'] = msg.subject
                data['text'] = msg.text
                lst.append(data)

            #     print(msg.date, msg.subject, len(msg.text or msg.html))
            await self.reply({'data': lst, 'request_id': 1, 'action': 'get_message'},)
        
   

class UserConsumer(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.PatchModelMixin,
        mixins.UpdateModelMixin,
        mixins.CreateModelMixin,
        mixins.DeleteModelMixin,
        GenericAsyncAPIConsumer,
):

    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [AllowAny,]
   
