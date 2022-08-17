import telebot, wikipedia, re

bot = telebot.TeleBot("5320929281:AAG3j5gHQdF_-eC4y3TuZupofq-zf3pJepQ")

# Устанавливаем язык Википедии
wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую 1000 слов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всё после последнейй точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для теста
        wikitext2 = ''

        # Проходимся по строкам, где нет равно (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей
                # переменной и возвращаем утерянные точки
                if(len((x.strip()))>3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'В энцикелопедии нет данных'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправь мне запрос')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Запрос принят')
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)