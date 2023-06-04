import telepot
from pprint import pprint
from telepot.loop import MessageLoop

bot = telepot.Bot('5432160114:AAEhYmtasG4NLCZeytfwlkZXTYJO13gpvGE')

def handle(msg):
    texto = msg['text']
    chat = msg['chat']
    uID = chat['id']
    if texto == "André":
        bot.sendMessage(uID, "Caca é fedida")

    else:
        bot.sendMessage(uID, "Comando incorreto. Fale quem é lindo!")

    
MessageLoop(bot, handle).run_as_thread()
