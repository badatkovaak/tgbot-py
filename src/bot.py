import telebot
import berserk
# import ast
import functions as func


with open('../token.txt', 'r', encoding='UTF-8') as f:
    BOT_TOKEN = str(f.readline().replace('\n', ''))
    LICHESS_TOKEN = f.readline().replace('\n', '')

bot = telebot.TeleBot(BOT_TOKEN)
session = berserk.TokenSession(token=LICHESS_TOKEN)
client = berserk.Client(session=session)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(commands=['test'])
# def test(message):
#     a_a = client.users.get_by_id('badatkovaak')
#     print(a_a)
#     # a = ast.literal_eval(a_a)
#     # print(a)
#     # print(type(a))
#     bot.send_message(message.chat.id, 'data')
#

@bot.message_handler(commands=['get'])
def lichess_get_profile(message):
    a_a = client.users.get_by_id('badatkovaak')
    bot.send_message(message.chat.id, func.formatted(a_a[0], tabs=5))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
