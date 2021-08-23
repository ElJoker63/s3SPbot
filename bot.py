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
<a href=""></a>

<b>Consumo nacional:</b>
<b>1. </b><a href="https://soft.uclv.edu.cu/">Software UCLV</a>
<b>2. </b><a href="http://red.uclv.cu/softlib">Repo UCLV</a>
<b>3. </b><a href="https://visuales.uclv.cu/">Visuales UCLV</a>
<b>4. </b><a href="http://android.uclv.edu.cu/">Android Store UCLV</a>
<b>5. </b><a href="http://ios.uclv.edu.cu/">iOS Store UCLV</a>
<b>6. </b><a href="https://mochila.uclv.cu/">La Mochila UCLV</a> 
<b>7. </b><a href="http://ftp.uij.edu.cu/">FTP Isla de la Juventud</a>
<b>8. </b><a href="http://download.jovenclub.cu/">Joven Club Descargas</a>
<b>9. </b><a href="https://mochila.cubava.cu/">La Mochila</a>
''', parse_mode = "html", disable_web_page_preview = True)

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, ftp))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()
