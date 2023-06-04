import telepot

from pprint import pprint

from telepot.loop import MessageLoop
bot = telepot.Bot("5432160114:AAEhYmtasG4NLCZeytfwlkZXTYJO13gpvGE")

def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()
user_id = 1877360398
bot.sendMessage(user_id, "Olá!!")
