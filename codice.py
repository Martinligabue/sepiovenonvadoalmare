import telepot
from telepot.loop import MessageLoop

"""alle 7 manda un messaggio nel gruppo"""       
piove=api.openweathermap.org/data/2.5/weather?q=Florence
"""non so come estrapolare se piove o meno: https://openweathermap.org/current"""
if(piove==1)
    bot.sendMessage(chat_id, "Non vado al mare")
else
    bot.sendMessage(chat_id, "Vado al mare")

bot = telepot.Bot('*** INSERT TOKEN ***')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
