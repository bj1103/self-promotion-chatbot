from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
from luis import getIntent

import random
import json
from messages import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('channel_access_token', None))
handler = WebhookHandler(os.getenv('channel_secret', None))

with open("./education.json") as f:
	education = json.load(f)
with open("./project.json") as f:
	projects = json.load(f)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def reply(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        reply_token = event.reply_token
        if event.message.text == '想了解你的學經歷！':
            flex_message = FlexSendMessage(
                alt_text='education',
                contents=education
            )
            line_bot_api.reply_message(
                reply_token,
                flex_message
            )
        elif event.message.text == '想了解你做過的project！':
            flex_message = FlexSendMessage(
                alt_text='projects',
                contents=projects
            )
            line_bot_api.reply_message(
                reply_token,
                flex_message
            )
        elif event.message.text == '想了解此Chatbot的設計及功能！':
            line_bot_api.reply_message(
                reply_token,
                TextSendMessage(text=manual)
            )
        else:
            intent = getIntent(event.message.text)
            if intent == 'None':
                text = "抱歉！功能尚未開發完全ＱＱ"
                line_bot_api.reply_message(
                    reply_token,
                    TextSendMessage(text=text)
                )
            elif intent == '介紹':
                text = self_introduction
                line_bot_api.reply_message(
                    reply_token,
                    TextSendMessage(text=text)
                )
            elif intent == '詢問專長':
                line_bot_api.reply_message(
                    reply_token,
                    [TextSendMessage(text=skill_1), TextSendMessage(text=skill_2)]
                )
            elif intent == '詢問特質':
                line_bot_api.reply_message(
                    reply_token,
                    [TextSendMessage(text=character_1), TextSendMessage(text=character_2)]
                )
            elif intent == '問候':
                line_bot_api.reply_message(
                    reply_token,
                    TextSendMessage(text=greet)
                )
            else:
                text = intent
                line_bot_api.reply_message(
                    reply_token,
                    TextSendMessage(text=text)
                )


if __name__ == "__main__":
    app.run()