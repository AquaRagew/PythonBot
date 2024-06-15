import webbrowser

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('7239615040:AAFteHrBtzTn7F1Mhx1AqJzbkOXd8d_S8U8')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт' )
    markup.row(btn1)
    btn2 = types.KeyboardButton('Видалити фото' )
    btn3 = types.KeyboardButton('Змінити текст')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Ку', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text =='Видалити фото':
        bot.send_message(message.chat.id, 'Delete')



@bot.message_handler(commands=['website'])
def site(message):
    webbrowser.open('https://www.google.com')


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Ky, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'Hello':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Видалити фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Змінити текст', callback_data='edit')
    markup.row(btn2, btn3)

    bot.reply_to(message, 'Ухтишка!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)






bot.infinity_polling()
