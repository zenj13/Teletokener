from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, InlineKeyboardButton, MenuButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ApplicationBuilder, MessageHandler, filters
import asyncio,tokener
#from detamod import Detaman
from deta import Deta
from tkuser import Tkuser
from tkman import Tkman
from tokeni import AToken

service_name = "testman"
active_cmd = {}
tasks_made = {}
deta_data_token = "d0xuy41v68a_97QYgZqGPUiwUPVAd6TD4kVPy6rGQnG4"
jwt_secret_key = "iwasbornandraisedbutcutfromadifferentcloth,lifewasn'tfunnywhenbeingcalledbrokewasajoke"
token_service = str()
#detaguy = Detaman(deta_data_token,"tokens_db")
detaguy = Deta(deta_data_token)
deta_userz = detaguy.Base("ayeuserz")
deta_tokenz = detaguy.Base("ayetokenz")


async def askToken(ask_txt,update):
    print(update)
    print("\n\n\n")
    button1 = InlineKeyboardButton(text='Get token', web_app=WebAppInfo('https://tokener-1-r6555868.deta.app/'))
    button2 = InlineKeyboardButton(text='write token',callback_data = "writetoken")
    keyboard = InlineKeyboardMarkup([[button1,button2]])
    await update.message.reply_text(ask_txt, reply_markup=keyboard)

async def processService(update):
    txt = update.message.text
    print(f"processing service: {txt}")

async def processToken(update):
    cid = update.effective_user.id
    tk = update.message.text
    print(f"processing token: {tk}")
    ausr = Tkuser(cid,service_name,deta_userz)
    global detaguy
    atoken = AToken(tk,jwt_secret_key)
    token_data = atoken.getId()
    #token_data = tokener.decode_token(tk,jwt_secret_key)
    if token_data == None:
        #await update.message.reply_text(f'sorry, token is expired or not good but you can make another one')
        await askToken("sorry, your token is faulty",update)
    else:
        #put_res = detaguy.putToken(cid,token_service,token_data,token_exp[extimestamp])
        tk_cid = Tkman(token_data,deta_tokenz)
        tk_stat = tk_cid.isValid()
        if tk_stat == None:
                await askToken("sorry, your token is off: ",update)
        elif tk_stat == False:
                await askToken("sorry, you token has already been used: ",update)
        elif tk_stat == True:
                tk_cid.validate()
                ausr.addUser(atoken,"process_service")
                await update.message.reply_text("You are free to use this service")
       # if put_res == None:
       #     await update.message.reply_text(f'token is bad, create another one')
       # else:
           # active_cmd[cid] = "process_service"
        #    await update.message.reply_text(f'your token is good but only for 1 day')

async def authToken(update):
    print('authing user')

async def chatMan(update,context):
    
    cid = update.effective_user.id
    await update.message.reply_text(f'pliz {cid} wait katono')
    print(f"\n\nuser id is: {cid}")
    #await asyncio.sleep(30)
    print(f"\n\nlets go eyes: {cid}\n")
    cidman = Tkuser(cid,service_name,deta_userz)
    iactive_cmd = cidman.getCmd()
    #if active_cmd[cid]== "process_token":
    if iactive_cmd == None or iactive_cmd=="process_token":
        print("processing token")
        await processToken(update)
    #elif active_cmd[cid] == "process_service":
    elif iactive_cmd == "process_service":
        await processService(update)
        print("service started")
    else:
        print("token error")

async def chatManCmd(update,context):
    asyncio.create_task(chatMan(update,context))

async def callback(update,context):
        query = update.callback_query
        cid = query.from_user.id
        cidman = Tkuser(cid,service_name,deta_userz)
        iactive_cmd = cidman.getCmd()
        print(query)
        if query.data=="writetoken":
            print("\n\n")
            #print(active_cmd[cid])
            print(iactive_cmd)
            #active_cmd[cid]= "process_token"
            await query.message.reply_text("please write token and send to me")
        else:
            await query.message.reply_text("error callback")

async def writeToken(update, context):
    print(update.message.text)



async def startCmd(update,context):
    cid = update.effective_user.id
    print("start started")
    cidman = Tkuser(cid,service_name,deta_userz)
    cmd = cidman.getCmd()
    print(update)
    if cmd == None:
        print("user error")
        await askToken("sorry, you are out of tokens: ",update)
    else:
        token_id = cidman.getTokenID()
        if token_id == None:
            await askToken("sorry, you don't have any token: ",update)
        else:
            tk_cid = Tkman(token_id,deta_tokenz)
            tk_stat = tk_cid.isValid()
            if tk_stat == None:
                await askToken("sorry, you token is off: ",update)
            #if tk_stat == False:
            #    await askToken("sorry, you token has already been used: ",update)
            #if tk_stat == True:
            else:
                await update.message.reply_text("You are free to use this service")


async def start(update, context):
    cid = update.effective_user.id
    #kb = [
    #    [KeyboardButton("Show me Google!", web_app=WebAppInfo("https://google.com"))]
    #]
   # await update.message.reply_text(f'pliz {cid} wait katono')
   # await asyncio.sleep(30)
    asyncio.create_task(startCmd(update,context))
    print("\n\nok off we go\n\n")

async def exstart(update,context):
    global active_cmd
    active_cmd[cid] = "nodata"

    mb = MenuButton('default')#, callback_data='command:data_to_send')

# Create a menu with the button
   

    button1 = InlineKeyboardButton(text='Get token', web_app=WebAppInfo('https://tokener-1-r6555868.deta.app/'))
    button2 = InlineKeyboardButton(text='write token',callback_data = "writetoken")
    keyboard = InlineKeyboardMarkup([[button1,button2]])
    await update.message.reply_text('Sorry, your tokens are finished:', reply_markup=keyboard)
   # await update.message.chat.set_menu_button(menu_button=mb)

async def runCmd(update,context):
    cid = update.effective_user.id
    task_made = asyncio.create_task(start(update,context))
    await task_made

async def xstartCmd(update,context):
    cid = update.effective_user.id
    #tasks_made[cid] =
    asyncio.create_task(start(update,context))
    #await task_made
    #runCmd(update,context)
    #asyncio.run(runCmd(update,context))
    #await task_made



def main():
    # Set up your bot token and create an Updater instance
    app = ApplicationBuilder().token('6274961154:AAG_G3E1mYVQ-AVL_YJUteIgmaUvWlzMxss').build()
    #updater = Updater(token=).Updater()#, use_context=True)
    #dispatcher = updater.dispatcher

    # Add command handlers
    #start_handler = CommandHandler('start', startCmd)
    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(filters.TEXT,callback=chatManCmd)
    app.add_handler(start_handler)
    app.add_handler(msg_handler)

    # Add callback query handler for button clicks
    callback_handler = CallbackQueryHandler(callback)
    app.add_handler(callback_handler)

    # Start the bot
    app.run_polling()
    #updater.idle()
    #loop = asyncio.get_event_loop()
    #loop.run_forever()

if __name__ == '__main__':
    main()