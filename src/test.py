import ast
import berserk
import functions

with open('../token.txt', 'r', encoding='UTF-8') as f:
    BOT_TOKEN = str(f.readline().replace('\n', ''))
    LICHESS_TOKEN = f.readline().replace('\n', '')

# bot = telebot.TeleBot(BOT_TOKEN)
session = berserk.TokenSession(token=LICHESS_TOKEN)
client = berserk.Client(session=session)
var = client.users.get_by_id('badatkovaak')
# print(var, type(var))
print(functions.format_list(var))
# print(ast.literal_eval(var))
