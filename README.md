# Self-Promotion Chatbot

## QRcode

* Notice 
  * 盡量使用手機與chatbot互動，能保證有完整的功能(ex. 電腦版的Line未必有支援選單服務)
  * Heroku上的app隔一陣子沒人使用會關機，因此chatbot的第一次回覆可能需要較長的時間

![qrcode](./qrcode.png)

## Chatbot介紹

### 概要

這是一個能夠將我介紹給其他人的Chatbot，能夠讓別人透過與chatbot的互動快速的了解我。其中promotion的內容包含了我對自己的個性認知、專長描述、學習歷程以及過去曾做過的projects。

### 架構

* 選單

  * 透過Line bot的rich menus提供使用者簡易的選單，內容包含
    * 個人github連結
    * 以Flex message用timeline的方式呈現學經歷
    * 以Flex message用水平滑動的視窗呈現過去的projects

* Chat message後端文字處理

  * 使用microsoft azure LUIS(language understanding)服務
    * [Language Understanding (LUIS)](https://azure.microsoft.com/zh-tw/services/cognitive-services/language-understanding-intelligent-service/)
  * 透過LUIS，可以解析使用者傳的message，並且去了解使用者的intent(意圖)，並讓chatbot根據意圖做出適當的回覆
    * Intent跟各類型Intent會有的Entity是事先定義好的，對定義完成的各Intent與Entity都給予範例後，LUIS會進行training，訓練後再Publish，即可作為Chatbot文字處理的後端，對使用者傳來的訊息做intent的預測
    * 雖然使用LUIS仍要對各個Intent提供一些範例，但LUIS能夠透過學習，透過這些範例產生更近一步的認知能力，因此無論是將同樣的句子換個方式說，或是將字詞換成其他意義接近的詞彙，LUIS皆有很高機率能夠將其intent辨識正確。一般Rule base的conversation，需要建立大量的rule來對使用者傳的訊息進行匹配，相比之下，使用LUIS來做訊息意圖判斷是便利且有效許多

  * 目前的chatbot尚未有較複雜的conversation flow，主要是將使用者傳送的訊息分為以下三種intent並進行相對應的回覆
    * 請chatbot進行自我介紹
    * 詢問chatbot我的專長、興趣
    * 詢問chatbot我的個人特質

## How to start

### Environment property

Fill in the following environment variables:

```
channel_access_token=
channel_secret=
predictionKey=
predictionEndpoint=
app_id=
```

### Test in local

1. Run `python app.py`
2. Open another terminal, run `ngrok http 5000`
3. Copy the ngrok url to LINE Developer Console and add `/callback` behind the url
4. Have fun!

### Deploy on Heroku

1. Run `heroku login -i`  to login heroku
2. Run `heroku git:remote -a <your_heroku_app_name> ` in the local directory with this repo
3. Set the environment variables list above on Heroku

```
heroku config:set channel_access_token=
heroku config:set channel_secret=
heroku config:set predictionKey=
heroku config:set predictionEndpoint=
heroku config:set app_id=
```

5. Run `git push heroku` , and the chatbot server will start
6. Copy the Heroku url to LINE Developer Console and add `/callback` behind the url
7. Have fun!