from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN="---NASCOSTO---"

#COPIARE E INCOLLARE DA QUI - IL TOKEN E' GIA' INSERITO

versione="0.0.1 alpha"
ultimoAggiornamento="14-10-2018"

def risposte(msg):
    try:
        chat_id=msg['chat']['id']
        text=msg['text']
    except:
        print("Exception:001")
        ##entra in questa eccezione se NON è avviato come comando diretto (digitato come comando e inviato)
    try:
        query_id, chat_id, text = telepot.glance(msg, flavor='callback_query')
        print(query_data)
    except:
        print("Exception:002")
        ##entra in questa eccezione se NON è stato premendo su un pulsante delle inlineKeyboard
    ##i try-except precedenti servono per assegnare, in qualunque circostanza, chat_id e text corettamente (in base al caso)
    
    home = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Vai al gruppo Home', url='')],
                ])

    feedback = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Vai in 'Home' e lascia il tuo feedback", url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ')],
                    [InlineKeyboardButton(text="Chiedi di voler contribuire al bot in 'Home'", url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ')]
                ])

    start = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Mostrami che cosa posso fare', callback_data='/help')],
                    [InlineKeyboardButton(text='Ho bisogno di assistenza', callback_data='/supporto')],
                ])

    supporto = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Supporto via Telegram', url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ'),
                    InlineKeyboardButton(text='Supporto via forum', callback_data='/forum')],
                    [InlineKeyboardButton(text='Leggi FAQ dal forum di Mozilla Italia', url='https://forum.mozillaitalia.org/index.php?board=9.0')]
                ])

    help = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Home', callback_data='/home'),
                    InlineKeyboardButton(text='Gruppi', callback_data='/gruppi'),
                    InlineKeyboardButton(text='Supporto', callback_data='/supporto')],
                    [InlineKeyboardButton(text='Collabora', callback_data='/collabora'),
                    InlineKeyboardButton(text='Vademecum', callback_data='/vademecum')],
                    [InlineKeyboardButton(text='News', callback_data='/news'),
                    InlineKeyboardButton(text='IoT', callback_data='/iot'),
                    InlineKeyboardButton(text='Developer', callback_data='/developer')],
                    [InlineKeyboardButton(text='Design', callback_data='/design'),
                    InlineKeyboardButton(text='Feedback', callback_data='/feedback'),
                    InlineKeyboardButton(text='Info', callback_data='/info')],
                    [InlineKeyboardButton(text='Call', callback_data='/call'), 
                    InlineKeyboardButton(text='Lista call', callback_data='/listacall'), 
                    InlineKeyboardButton(text='Prossima call', callback_data='/prossimacall')],
                ])

    '''
    nome_nome = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Testo bottone (riga 1, col 1)', callback_data='/comando'),
                    InlineKeyboardButton(text='Testo bottone 2 (riga 1, col 2)', callback_data='/comando2')],
                    [InlineKeyboardButton(text='Testo bottone 3 (riga 2, col 1-2)', url='https://t.me/')],
                ])
    '''

    if text=="/start":
        bot.sendMessage(chat_id, "Benvenuto")
    elif text=="/help":
        bot.sendMessage(chat_id, "Aiuto")
    else:
        bot.sendMessage(chat_id, "Errore: comando non riconosciuto", reply_markup=start)


bot=telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': risposte, 'callback_query': risposte}).run_as_thread()

while 1:
    time.sleep(10)
