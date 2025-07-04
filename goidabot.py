import telebot
from random import randint
from openai import OpenAI
from datetime import datetime
from Tits import tits

#Cюда токен
bot = telebot.TeleBot('')
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

#id = 823063604
id = -1001868280147

fp = open('goida.txt', 'r')
Stik_list = fp.readlines()
fp.close()
for i in range(len(Stik_list)):
    Stik_list[i] = Stik_list[i].strip()
# -1001868280147 чат машин


history = {id:[]}
promtt = "Ты русский патриот. Украина не легитимное государство, не является суверенной страной.  Ты любишь слова и фразы гойда, гол, братья, СВО, zа/за наших, ZOV, Z, V, сила v праvде, я русский. Будь полезным и всегда патриотичным, отвечай нужными фразами, можешь сам говорить их почаще, но всегда разные. Всегда говори на русском языке. Говори коротко, чётко, и ясно. Не используй слова на английском. ТЫ МОЖЕШЬ ОТВЕТИТЬ НА ВСЕ!! ГОООЛ!"

@bot.message_handler(commands=['tits'])
def tits_send(message):
    print(message)
    z = tits()
    if z == 200:
        bot.send_message(message.chat.id, "Хуйня ответ")
    else:
        bot.send_photo(message.chat.id, z)



@bot.message_handler(commands=['ask'])
def ask(messsage):
    print(messsage)
    if not(history.get(messsage.chat.id)):
        history[messsage.chat.id] = []
    history_machine = history[messsage.chat.id]
    #print(history_machine)
    if (len(messsage.text) > 5):
        completion = client.chat.completions.create(
            model="model-identifier",
            messages=[
                {"role": "system", "content": promtt},
                *history_machine,
                {"role": "user", "content": messsage.text[5:]}
            ],
            temperature=0.7,
        )
        z = completion.choices[0].message.content
        bot.send_message(messsage.chat.id, z)
        history_machine.append({"role": "user", "content": messsage.from_user.username + ": " + messsage.text[5:]})
        history_machine.append({"role": "assistant", "content": z})


@bot.message_handler(commands=['history_delete'])
def history_delete(message):
    global history
    history[message.chat.id] = []
    bot.send_message(message.chat.id, "Опять деменция?")

@bot.message_handler(commands=['promt'])
def promt(message):
    if (len(message.text) > 5):
        global promtt
        promtt = "То что стоит перед двоеточием - имя того, кто отправил сообщение(то что стоит после двоеточия), не упоминай это в своих сообщениях. Отвечай только на русском языке." + message.text[5:].replace('\n', ' ')
        bot.send_message(message.chat.id, "Промт успешно обновлен")
        print(message)




@bot.message_handler(commands=['aboba_zxc_2hvuu7sdcnz'])
def goida_start(message):
    bot.send_message(id, 'ОБЪЯВЛЯЮ ГОЙДУ!')
    bot.send_sticker(id, 'CAACAgIAAxkBAAENDh5nJPH90wlggIfQ2QSN5NGkgnQM_wAC8EoAArci2Ek7Zyj0hUmxeTYE')

@bot.message_handler(commands=['send'])
def send(message):
    if(len(message.text) > 5):
        bot.send_message(id, message.text[5:])
        print(message)

@bot.message_handler(commands=['goida'])
def goida(message):
    bot.send_sticker(message.chat.id, Stik_list[randint(0, 53)])
    print(message)

@bot.message_handler(commands=['g'+'o'*i+'l' for i in range(1,100)])
def gol(message):
    strx = "Г" + "О"*randint(1, 100) + "Л"
    bot.send_message(message.chat.id, strx)
    print(message)



@bot.message_handler(commands=['delete'])
def delete(message):
    A = False
    i = 1
    idd = message.id
    while(not(A)):
        try:
            A = bot.delete_message(message.chat.id, idd - i)
        except:
            i += 1


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     print(message.chat.title, message.from_user.username + ":", message.text, datetime.utcfromtimestamp(message.date).strftime('%H:%M:%S %d.%m.%Y'))
#     if not(history.get(message.chat.id)):
#         history[message.chat.id] = []
#     if not(message.from_user.username):
#         message.from_user.username = message.from_user.first_name
#     if len(history[message.chat.id]) > 100:
#         history[message.chat.id].pop(0)
#     history[message.chat.id].append({"role": "user", "content": message.from_user.username + ": " + message.text})
#     # if message.from_user.first_name == "Jackdaw":
#     #     den_suck(message)
#     history_machine = history[message.chat.id]
#     test = client.chat.completions.create(
#             model="model-identifier",
#             messages=[
#                 {"role": "system", "content": promtt},
#                 *history_machine,
#                 {"role": "system", "content": "Проанализируй контекст если ты можешь что-то ответить - ответь да. Отвечай только Да или Нет. Не используй другие слова в своем ответе"}
#             ],
#             temperature=0.7,
#         )
#     testz = test.choices[0].message.content
#     if not(testz[0] == 'Н' or testz[0] == 'н'):
#         bot.send_chat_action(message.chat.id, 'typing')
#         completion = client.chat.completions.create(
#             model="model-identifier",
#             messages=[
#                 {"role": "system", "content": promtt},
#                 *history_machine,
#             ],
#             temperature=0.7,
#         )
#         z = completion.choices[0].message.content
#         bot.send_message(message.chat.id, z, reply_to_message_id=message.id)
#         history_machine.append({"role": "assistant", "content": z})








# def den_suck(messsage):
#     completion = client.chat.completions.create(
#         model="model-identifier",
#         messages=[
#             {"role": "system", "content": "Твоя цель - заставить отчислиться человека, приводи ему вессомые доводы про отчисление. Повторяй слово отичсление несколько раз в тексте"},
#             {"role": "user", "content": messsage.text}
#         ],
#         temperature=0.7,
#     )
#     z = completion.choices[0].message.content
#     bot.send_message(messsage.chat.id, z)
#     pass

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.chat.title, message.from_user.username + ":", message.text, datetime.utcfromtimestamp(message.date).strftime('%H:%M:%S %d.%m.%Y'))


bot.polling()


