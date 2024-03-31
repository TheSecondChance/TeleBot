import telebot
from telebot import types
from telebot.types import WebAppInfo
import os



BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button = types.KeyboardButton('Form', web_app=WebAppInfo(url='https://hojigari.get-alpha.tech'))
  markup.add(button)
  bot.send_message(message.chat.id, "Welcome to My Bot... ", reply_markup=markup)


 
@bot.message_handler(commands=["ToRegister"])
def send_game_message(message):
  markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
  btn1 = types.KeyboardButton("/Student")
  btn2 = types.KeyboardButton("/Register")
  btn3 = types.KeyboardButton("/close")
  markup.add(btn1, btn2, btn3)
  bot.send_message(chat_id=message.chat.id, text="what do you want",
                   reply_markup=markup)

@bot.message_handler(commands=["close"])
def send_game_message(message):
  markup = types.ReplyKeyboardRemove(selective=False)
  bot.send_message(chat_id=message.chat.id, text="see you agin",
                   reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='https://t.me/eyasu_dev'
        )
    )
    bot.send_message(
        message.chat.id,
        '1) To receive a list of available command press /ToRegister.\n ' +
        '2) Click on.\n' +
        '3) You will receive a message containing information regarding the source, ' +
        'contact.\n' +
        '4) Click “Update” to receive the current information regarding the request. ',
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text + " not correcte")
 
 

bot.infinity_polling()