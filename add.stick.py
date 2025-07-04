import telebot
bot = telebot.TeleBot('7785940914:AAE8_7LOtPBfr4UZjWTAHkLZ2_yLbWhKD4E')

Stik_list = []


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def echo_all(message):
    fp = open('goida.txt', 'a')
    #print(message.sticker.file_id)
    Stik_list.append(message.sticker.file_id)
    fp.write(message.sticker.file_id+'\n')
    fp.close()

bot.polling()