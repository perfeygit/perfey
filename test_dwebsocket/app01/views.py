import json
from django.shortcuts import render, HttpResponse, redirect
from dwebsocket import require_websocket,accept_websocket
from dwebsocket.websocket import WebSocket

from django.conf import settings
ip = '127.0.0.1:8000'

# Create your views here.
user_socket_dict = {}


@require_websocket
def ws(request, user=None):
    if request.is_websocket():
        user_socket = request.websocket  # type:WebSocket
        user_socket_dict[user] = user_socket
        while 1:
            try:
                user_socket.send(json.dumps([i for i in user_socket_dict]))
                msg = user_socket.wait()
                msg = json.loads(msg)
                to_user = msg.get('to_user')
                content = msg.get('msg')
                usocket = user_socket_dict.get(to_user)
                recv_msg = {'from_user': user, 'msg': content, }
                if usocket:
                    usocket.send(json.dumps(recv_msg))
                else:
                    for usocket in user_socket_dict.values():
                        if usocket != user_socket:  # 群发,对除了当前自己的websocket连发送消息
                            usocket.send(json.dumps(recv_msg))
            except:
                pass



def index(request):
    return render(request, 'index.html',{'ip':ip})
