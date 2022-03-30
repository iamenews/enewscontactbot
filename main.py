import os
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from keep_alive import keep_alive

apikey = os.environ['apikey']
#apikeyforbot

bot = telebot.TeleBot(apikey, parse_mode=None)

@bot.message_handler(commands='start')
def start(m):
  subscribe = [[InlineKeyboardButton('Subscribe to E-News!', url='t.me/enewssg')]]
  bot.send_message(m.chat.id, 'Hi there! This bot helps you to contact E-News administrators. You can leave a message below to contact them!\n Not too sure what to do? You can run the /help command!', reply_markup=InlineKeyboardMarkup(subscribe))

@bot.message_handler(commands='help')
def help(m):
  status = [[InlineKeyboardButton('See bot status',url='https://botstatus.enews.link/')]]
  bot.send_message(m.chat.id, "Welcome to the help menu. There is really only one command on this bot, its /start. Run start, and then type a message below. That message will be sent to the team, and we will reply as soon as we can. \n If the bot is not working, you can click below to check out the status.", reply_markup=InlineKeyboardMarkup(status))
  bot.send_message(m.chat.id,"By the way, if you are trying to find our channels, we have linked them below.\n t.me/enewssg\n t.me/enewslounge ")
  

@bot.message_handler(commands='reply')
def reply(m):
  if m.chat.id == 609843193:
    msg = bot.send_message(609843193, 'Send the ID followed by message with an underscore between them.')
    bot.register_next_step_handler(msg, replytouser)
  else:
    bot.send_message(m.chat.id, "Sorry, you can't use this command.")
def replytouser(m):
  text = m.text
  ID = text.rpartition('_')[0]
  message = text.rpartition('_')[2]
  bot.send_message(int(ID), f'{message}')
  bot.send_message(609843193, 'Message has been sent.')
  
@bot.message_handler(func=lambda m: True)
def gettext(m):
  bot.send_message(609843193, 
f"{m.chat.id} \n{m.from_user.first_name} sent a message:")
  bot.send_message(609843193, m.text)
  bot.send_message(m.chat.id, 'Done! We have passed on your message - we hope to resolve your issue soon!')

keep_alive()
bot.infinity_polling()