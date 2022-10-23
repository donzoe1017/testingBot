from cProfile import label
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
from linebot.models import *

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
    #print(request)
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
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='https://liff.line.me/'+liff_id))
                    except:
                        print(err.message)
                elif(event.message.text =="選單"):
                    line_bot_api.reply_message(
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text = 'Buttons template',
                            template = ButtonsTemplate(
                                title = '選單',
                                text = '請選擇行動',
                                actions = [
                                    URITemplateAction(
                                        label = '製作遊戲',
                                        uri = 'http://140.134.26.66:5051/'
                                    ),
                                    MessageTemplateAction(
                                        label='教學引導',
                                        text='教我如何操作'
                                    ),
                                    MessageTemplateAction(
                                        label='成品範例',
                                        text='成品範例'
                                    )
                                    #,URITemplateAction(
                                    #    label='我是DD',
                                    #    uri = 'https://holodex.net'
                                    #)
                                    #PostbackTemplateAction(
                                    #    label='我是DD',
                                    #    data='看V傳送門')
                                ]
                            )
                        )
                    )
                elif(event.message.text =="教我如何操作"):
                    line_bot_api.reply_message(event.reply_token,
                        TemplateSendMessage(
                            alt_text = "教學旋轉木馬模塊",
                            template = CarouselTemplate(
                                columns = [
                                    CarouselColumn(
                                        thumbnail_image_url = 'https://cdn.discordapp.com/attachments/783700163017441330/967678889382010900/unknown.png',
                                        title = '登入頁面',
                                        text = '登入帳號後即可開始製作',
                                        actions = [
                                            URITemplateAction(
                                                label = '觀看全圖',
                                                uri = 'https://cdn.discordapp.com/attachments/783700163017441330/967678889382010900/unknown.png'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                        thumbnail_image_url = 'https://cdn.discordapp.com/attachments/783700163017441330/967678631428096010/unknown.png',
                                        title = '選單頁面',
                                        text = '透過左右滑動選擇要製作遊戲',
                                        actions = [
                                            URITemplateAction(
                                                label = '觀看全圖',
                                                uri = 'https://cdn.discordapp.com/attachments/783700163017441330/967678631428096010/unknown.png'
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                    )
                elif(event.message.text =="成品範例"):
                    line_bot_api.reply_message(event.reply_token,
                        TemplateSendMessage(
                            alt_text = '成品旋轉木馬',
                            template = ImageCarouselTemplate(
                                columns = [
                                    ImageCarouselColumn(
                                        image_url="https://cdn.discordapp.com/attachments/783700163017441330/967686181003345961/toy1.png",
                                        action=URITemplateAction(
                                            label="接水果",
                                            uri = "https://cdn.discordapp.com/attachments/783700163017441330/967686181003345961/toy1.png"
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url="https://cdn.discordapp.com/attachments/783700163017441330/967686181473120276/gift1.png",
                                        action=URITemplateAction(
                                            label="戳戳樂",
                                            uri = "https://cdn.discordapp.com/attachments/783700163017441330/967686181473120276/gift1.png"
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url="https://cdn.discordapp.com/attachments/783700163017441330/967686181720571994/mom1.png",
                                        action=URITemplateAction(
                                            label="做菜模擬",
                                            uri = "https://cdn.discordapp.com/attachments/783700163017441330/967686181720571994/mom1.png"
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url="https://cdn.discordapp.com/attachments/783700163017441330/967686181938683934/newYear1.png",
                                        action=URITemplateAction(
                                            label="打氣球",
                                            uri = "https://cdn.discordapp.com/attachments/783700163017441330/967686181938683934/newYear1.png"
                                        )
                                    )
                                ]
                            )
                        )
                    )
                else:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )
        return HttpResponse()
    
    else:
        return HttpResponseBadRequest()
