import telebot
from telebot import types
import config as cfg
import vkscrap 
import os, os.path

bot = telebot.TeleBot(cfg.TOKEN_TG)

#Стартовое состояние
@bot.message_handler(commands=['start', 'back'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('💻 Начать парсинг VK', '❓ О боте')
    keyboard.row('💡 Помощь', '📬 Моя подписка')
    bot.send_message(message.chat.id, 'Привет! Выбери один из вариантов снизу:', reply_markup=keyboard)

@bot.message_handler(commands=['scrapvk'])
def start_scrap(message):
    #Вводим коротки(й, е) адрес(а)
    step = bot.send_message(message.chat.id, "<b>Введите короткий адрес пользователя или сообщества группы VK</b>\nНапример:\n<code>https://vk.com/dobriememes</code> - ссылка\n<code>dobriememes</code> - короткий адреc.", parse_mode='html')
    bot.register_next_step_handler(step, set_domain)
def set_domain(message):
    domain = message.text
    with open('data/domain.csv', "w", encoding='utf-8') as file:
        file.write(domain)
    step_time = bot.send_message(message.chat.id, "<b>Введите число в минутах для обозначения промежутка между парсингом: </b>", parse_mode='html')
    bot.register_next_step_handler(step_time, set_time)
def set_time(message):
    sleep_time = message.text
    with open("data/sleep.text", "w", encoding='utf-8') as file:
        file.write(sleep_time)
    vkscrap.vk_parser()


@bot.message_handler(content_types=['text'])
def func(message):
    #Обработка кнопки "Начать парсинг"
    if(message.text == "💻 Начать парсинг VK"):
        bot.send_message(message.chat.id, "<b>Введите /scrapvk, чтобы начать\n</b>", parse_mode='html')
    #Обработка кнопки "Помощь"
    if(message.text == "💡 Помощь"):
        bot.send_message(message.chat.id, "<b>Введите <code>/scrapvk</code>:", parse_mode='html')
    #Обработка кнопки "О боте"
    if(message.text == "❓ О боте"):
        bot.send_message(message.chat.id, "<b>Version:</b><i> 1.0.0</i>", parse_mode='html')
    #Обработка кнопки "Моя подписка"
    if(message.text == "📬 Моя подписка"):
        bot.send_message(message.chat.id, "<b>Выберите один из вариантов:\n\n</b><i>Тут будут варианты:</i>", parse_mode='html')

#Парсинг с настройками
        
#Начало работы бота

if __name__ == '__main__':
    # try:
    bot.polling(none_stop=True)
    # except:
    #     pass
    