import telebot
import certifi
import requests
import json
import urllib3

with open('data/config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

bot = telebot.TeleBot(config[''])

for channel in config['CHANNEL_LOGIN']:
            bot.send_photo(channel, img_data)
            bot.send_message(message.chat.id, text)
            time.sleep(sleep_time * 60)
