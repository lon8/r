import telebot
from telebot import types
import config as cfg
import vkscrap
import os, os.path

bot = telebot.TeleBot(cfg.TOKEN_TG)

#Обработчик входящих сообщений
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Привет, дорогой пользователь.</b>\n\n<code>Список команд бота:</code>\n\n1. /scrap - <i>Начать парсинг</i>\n2. /subscribe - <i>Моя подписка</i>\n3. /about - <i>О боте</i>\n4. /back - <i>Вернуться на главную</i>\n5. /help - <i>Просмотр команд</i>", parse_mode='html')

@bot.message_handler(commands=['scrap'])
def start(message):
    bot.send_message(message.chat.id, "<code>Выберите вариант парсинга:</code>\n\n1. /scrapvk - <i>Парсинг VK</i>\n2. /scraptg - <i>Парсинг Telegram</i>\n", parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "<code>Список команд бота:</code>\n\n1. /scrap - <i>Начать парсинг</i>\n2. /subscribe - <i>Моя подписка</i>\n3. /about - <i>О боте</i>\n4. /back - <i>Вернуться на главную</i>\n5. /help - <i>Просмотр команд</i>", parse_mode='html')

@bot.message_handler(commands=['about'])
def start(message):
    bot.send_message(message.chat.id, "<b>Version:</b><i> 1.0.0</i>", parse_mode='html')

@bot.message_handler(commands=['scrapvk'])
def start(message):
    bot.send_message(message.chat.id, "<b>Введите короткий адрес пользователя или сообщества группы VK</b>\nНапример:\n<code>https://vk.com/dobriememes</code> - ссылка\n<code>dobriememes</code> - короткий адреc.", parse_mode='html')
    @bot.message_handler(content_types=['text'])
    def domain_text(m):
        domain = m.text
        with open('data/domain.text', 'w', encoding='utf-8') as file:
            file.write(domain)
        vkscrap.vk_parser()
        


if __name__ == '__main__':
    # try:
    bot.polling(none_stop=True)
    # except:
    #     pass
    