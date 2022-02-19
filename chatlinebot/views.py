from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)

liff_api = LIFF(settings.LINE_CHANNEL_ACCESS_TOKEN)

'''
#import pymongo
from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient(host=mongodb+srv://donzoe1017:cxz99856@cluster0.t5qzo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority,
                      port=int(port),
                      username=donzoe1017,
                      password=cxz99856
                     )
 db_handle = client['linebot']
 return db_handle, client
'''
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
'''
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    
    else:
        return HttpResponseBadRequest()
'''

@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if(event.message.text[:5] == "https"):
                    try:
                        #新增LIFF頁面到LINEBOT中，取得liff id
                        liff_id = liff_api.add(view_type="full", view_url=event.message.text)
                        print(liff_id)
                        line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text='https://liff.line.me/'+liff_id))
                    except:
                        print(err.message)
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    
    else:
        return HttpResponseBadRequest()
