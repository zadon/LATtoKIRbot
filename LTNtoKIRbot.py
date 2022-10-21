import telebot
from transliterate import translit
from googletrans import Translator

bot = telebot.TeleBot('5651239800:AAHGSDVuPL7TzbgzcUuLry0kGmvU-0cw3Wo')

translator = Translator()

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, '')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = translit(message.text, 'mn')
    text_trans = translator.translate(text, dest='ru', src='mn')

    bot.send_message(message.chat.id, text_trans.text)

bot.polling(none_stop=True, interval=0)

