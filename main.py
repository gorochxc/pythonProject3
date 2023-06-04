import telebot
# python main.py

bot = telebot.TeleBot('6188027868:AAFYku6MpTzL0rUL250FkE_XZsRrqi90fPI')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Приветвую тебя,<b>{message.from_user.first_name} </b> добро пожаловать в наш магазин.Вот наши комманды;\n/vk-Наша группа вк;\n/a-Ассартимент ;\n/admin-Администратор ;'
    bot.send_message(message.chat.id,mess,parse_mode='html')
# @bot.message_handler(commands=['a'])
# def command(message):
#     dd=f"Цена каждого стикера 10.р"
#     photo=open('хуйня1.png','rb')
#     photo2 = open('хуйня2.png','rb')
#     photo3= open('хуйня3.png','rb')
#     bot.send_message(message.chat.id, dd, parse_mode='html')
#     bot.send_message(message.chat.id, "Итто",parse_mode='html')
#     bot.send_photo(message.chat.id,photo)
#     bot.send_message(message.chat.id, "Чжун Ли", parse_mode='html')
#     bot.send_photo(message.chat.id, photo2)
#     bot.send_message(message.chat.id, "Кэйа", parse_mode='html')
#     bot.send_photo(message.chat.id, photo3)
#     bot.send_message(message.chat.id, "если выбрали то оброщаться по адресу:@l_lama_l(https://t.me/l_lama_l)", parse_mode='html')
@bot.message_handler(commands=['vk'])
def asd(message):
    bot.send_message(message.chat.id, "Вот наша группа вк: https://vk.com/club220437556", parse_mode='html')
@bot.message_handler(commands=['admin'])
def xcs(message):
    bot.send_message(message.chat.id, "Вот наш администратор готовый вас выслушать: @l_lama_l  ", parse_mode='html')
@bot.message_handler()
def add(message):
        bot.send_message(message.chat.id, "Я не знаю эту команду", parse_mode='html')

bot.polling(none_stop=True)

