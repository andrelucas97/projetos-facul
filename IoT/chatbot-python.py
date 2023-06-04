import telepot

from pprint import pprint

from telepot.loop import MessageLoop
bot = telepot.Bot("5326670860:AAE_m-QDSWCDn_WGXUVh37AV0LYpSPi43jY")
def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()
user_id = 1877360398
bot.sendMessage(user_id, "Olá!!")
