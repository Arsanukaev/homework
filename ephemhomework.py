from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
def hello(bot, update):
    print('Привет')

def main():
    mybot = Updater('808049629:AAHXH6XLn_2HpMGsgUBn9y0TCI2mn22mJ8A', request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", hello))
    mybot.start_polling()
    mybot.idle()
main()

