from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("El bot esta funcionando!")

def ftp(update, context):
    msg = update.message.text
    if str(msg).__contains__("ftp"):
        update.message.reply_text(
        '''
<b>Libres de consumo:</b>
<b>1. </b><a href="http://ftp.udg.co.cu/">FTP Granma</a>
<b>2. </b><a href="http://ftp.uo.edu.cu/">FTP Santiago</a>   

Consumo nacional: 1. Software UCLV (https://soft.uclv.edu.cu/) 
2. Repo UCLV (http://red.uclv.cu/softlib) 
3. Visuales UCLV (https://visuales.uclv.cu/) 
4. Android Store UCLV (http://android.uclv.edu.cu/) 
5. iOS Store UCLV (http://ios.uclv.edu.cu/) 6. 
La Mochila UCLV (https://mochila.uclv.cu/) 
7. FTP Isla de la Juventud (http://ftp.uij.edu.cu/) 
8. Joven Club Descargas (http://download.jovenclub.cu/) 
9. La Mochila (https://mochila.cubava.cu/)
''', parse_mode = "html", disable_web_page_preview = True)

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, ftp))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()
