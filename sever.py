from flask import (Flask, request , abort,render_template)
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError


app = Flask(__name__)

line_bot_api = LineBotApi('8G0CdpifvSTnzWJRoK8sxDHEc67YxlLgPiaLLwk/rXO2s4+fyopQh48ioZBQa1g2Jm23JfCcqbz6XqFM/lhk9VaMJVwKHgKN0/C8J0WObTnhYHEn7T9c+0PZeh0Nppfl1s9Kg5/QyvTilXlkciH8xQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b584cdb1b112abe097e5a0da99903682') #b584cdb1b112abe097e5a0da99903682




@app.route('/')
def index():
    return render_template("index.html")

@app.route("/callback",methods = ['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text =True)

    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)
    
    return 'Ok!!!'

@handler.default()
def default(event):
    print('捕捉事件:',event )

if __name__ =="__main__":
    app.run(debug= True,host = "127.0.0.1",port=5000)