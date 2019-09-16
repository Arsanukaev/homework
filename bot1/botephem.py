from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import date
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
today = date.today()
def hello(bot, update):
    print('Привет!')
    update.message.reply_text("Привет")
    
def mars(bot, update):
    myplanet = update.message.text
    print(myplanet)
    if myplanet == "Mars":
        mymars = ephem.Mars(today)
        update.message.reply_text(f'{mymars}')
        const = ephem.constellation(mymars)
        update.message.reply_text(f'{const}')
    elif myplanet == "Mercury":
        myMercury = ephem.Mercury(today)
        update.message.reply_text(f'{myMercury}')
        const2 = ephem.constellation(myMercury)
        update.message.reply_text(f'{const2}')
    elif myplanet == "Venus":
        myVenus = ephem.Venus(today)
        update.message.reply_text(f'{myVenus}')
        const3 = ephem.constellation(myVenus)
        update.message.reply_text(f'{const3}')
    elif myplanet == "Jupiter":
        myJupiter = ephem.Jupiter(today)
        update.message.reply_text(f'{myJupiter}')
        const4 = ephem.constellation(myJupiter)
        update.message.reply_text(f'{const4}')
    elif myplanet == "Saturn":
        mySaturn = ephem.Saturn(today)
        update.message.reply_text(f'{mySaturn}')
        const5 = ephem.constellation(mySaturn)
        update.message.reply_text(f'{const5}')
    elif myplanet == "Uranus":
        myUranus = ephem.Uranus(today)
        update.message.reply_text(f'{myUranus}')
        const6 = ephem.constellation(myUranus)
        update.message.reply_text(f'{const6}')
    elif myplanet == "Neptune":
        myNeptune = ephem.Neptune(today)
        update.message.reply_text(f'{myNeptune}')
        const7 = ephem.constellation(myNeptune)
        update.message.reply_text(f'{const7}')
    elif myplanet == "Pluto":
        myPluto = ephem.Pluto(today)
        update.message.reply_text(f'{myPluto}')
        const8 = ephem.constellation(myPluto)
        update.message.reply_text(f'{const8}')
    else: 
        update.message.reply_text("Нет такой планеты!")

def help(bot, update):
    update.message.reply_text('Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto')

def main():
    mybot = Updater('808049629:AAHXH6XLn_2HpMGsgUBn9y0TCI2mn22mJ8A')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", hello))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, mars))
   
    mybot.start_polling()
    mybot.idle()
main()