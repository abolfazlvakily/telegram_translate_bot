import telebot
from telebot import types
from googletrans import Translator

translator = Translator()
bot_token = 'this is my token'
bot = telebot.TeleBot(token=bot_token)


class Command(object):
    START = 'start'
    ABOUT_ME = 'درباره_برنامه_نویس'
    HELP = 'منو_راهنما'
    TRANSLATE = 'ترجمه'


@bot.message_handler(commands=[Command.START, Command.HELP])
def help(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/' + Command.ABOUT_ME)
    itembtnv = types.KeyboardButton('/' + Command.HELP)
    itembtnc = types.KeyboardButton('/' + Command.TRANSLATE)
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc)
    bot.send_message(message.chat.id, "یکی از ابزار های زیر را انتخاب نمایید", reply_markup=markup)


@bot.message_handler(commands=[Command.ABOUT_ME])
def welcome(message):
    txt = '''
    سلام من وکیلی هستم
    برنامه نویس پایتون
    ربات قراره امکانات خیلی خوبی رو در اختیار تون قرار بده
    '''
    bot.reply_to(message, txt)


@bot.message_handler(commands=[Command.TRANSLATE])
def translate(message):
    bot.send_message(message.chat.id, 'بنویسید')
    bot.register_next_step_handler(message, _translate)


def _translate(message):
    t = translator.translate(message.text, dest='fa')
    bot.reply_to(message, t.text)


bot.polling()
