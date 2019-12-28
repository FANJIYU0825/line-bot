from flask import (Flask, render_template, request as rq, abort)
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import InvalidSignatureError


main_app = Flask(__name__, static_folder='.', static_url_path='')  #
# main_app.debug = True
line_bot_api = LineBotApi('rMF6DRuJRheVOnz7zPrtl7goR7xv46dMrFwlN0zCdh4EG7ptJFG658pV6Y07R8XtJm23JfCcqbz6XqFM/lhk9VaMJVwKHgKN0/C8J0WObTkSv6G1zeueYqH4PdEH+hyXBRuJb75yLf3eOJHOUCvX7AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b584cdb1b112abe097e5a0da99903682')  # ?  318797af646feaa757db0b6c6e08561c


@main_app.route('/', methods=["POST", "GET"])
def index():
	return render_template('index.html')  # main_app.send_static_file


@main_app.route('/callback', methods=["POST", "GET"])
def callback():
	signature = rq.headers['X-Line-Signature']
	body = rq.get_data(as_text=True)

	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'


@handler.default()
def default(event):
	print(f'{event} event catched')


if __name__ == "__main__":
	main_app.run(debug=True)  # , host='127.0.0.1', port=80