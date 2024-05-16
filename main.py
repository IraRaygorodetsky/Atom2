import telebot
from telebot import types

bot = telebot.TeleBot('7186628437:AAGVH4cLVsDk-WVbBAEllruJZd09pSrdduc')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Карточка 1')
    btn2 = types.KeyboardButton('Карточка 2')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Карточка 3')
    btn4 = types.KeyboardButton('Карточка 4')
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton('Карточка 5')
    btn6 = types.KeyboardButton('Карточка 6')
    markup.row(btn5, btn6)
    btn7 = types.KeyboardButton('Завершить игру')
    markup.row(btn7)
    #bot.send_message(message.chat.id, 'видео', reply_markup=markup)
    file = open('./startup.mp4', 'rb')
    bot.send_video(message.chat.id, file, 107, 1080, 1920, timeout=1000, reply_markup=markup)
    bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('1.jpg', 'rb')),
                                           telebot.types.InputMediaPhoto(open('2.jpg', 'rb')),
                                           telebot.types.InputMediaPhoto(open('3.jpg', 'rb')),
                                           telebot.types.InputMediaPhoto(open('4.jpg', 'rb')),
                                           telebot.types.InputMediaPhoto(open('5.jpg', 'rb')),
                                           telebot.types.InputMediaPhoto(open('6.jpg', 'rb'))])
    bot.register_next_step_handler(message, main)

#bot.send_video(message.chat.id, file, 31, 1080, 1920, timeout=1000)


@bot.message_handler()
def main(message):
    global stop
    if message.text.lower() == 'карточка 1':
        file = open('./1АНТИЧНОСТЬ.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'Введите код без пробелов')
        stop = 0
    elif message.text.lower() == 'античность':
        file = open('./12.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'карточка 2':
        file = open('./2ХИМИЯ.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'Введите код без пробелов')
        stop = 0
    elif message.text.lower() == 'химия':
        file = open('./22.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        file = open('./Таблица.jpeg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'карточка 3':
        file = open('./3ЧАСТИЦА.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'Введите код без пробелов')
        stop = 0
    elif message.text.lower() == 'частица':
        file = open('./32.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'карточка 4':
        file = open('./4ВОДОРОД.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'Введите код без пробелов')
        stop = 0
    elif message.text.lower() == 'водород':
        file = open('./42.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'карточка 5':
        file = open('./5БУДУЩЕЕ.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'Введите код без пробелов')
        stop = 0
    elif message.text.lower() == 'будущее':
        file = open('./52.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'карточка 6':
        file = open('./6ЛЕДОКОЛ.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'Введите код без пробелов')
        stop = 0
    elif message.text.lower() == 'ледокол':
        file = open('./62.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'наука':
        file = open('./63.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'завершить игру':
        bot.send_message(message.chat.id, 'Введите код без пробелов')
        stop = 1
    elif message.text.lower() == 'атом' and stop == 1:
        bot.send_message(message.chat.id, 'Код верный')
        #bot.send_message(message.chat.id, 'видео')
        file = open('./fingood.mp4', 'rb')
        bot.send_video(message.chat.id, file, 107, 1080, 1920, timeout=1000)
    elif message.text.lower() != 'атом' and stop == 1:
        bot.send_message(message.chat.id, 'Код неверный, попробуйте ещё 1 раз')
        stop = 2
    elif message.text.lower() != 'атом' and stop == 2:
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Код неверный', reply_markup = a)
        #bot.send_message(message.chat.id, 'видео')
        file = open('./finbed.mp4', 'rb')
        bot.send_video(message.chat.id, file, 107, 1080, 1920, timeout=1000)
    else:
        bot.send_message(message.chat.id, 'Код не найден')

bot.polling(none_stop= True)




