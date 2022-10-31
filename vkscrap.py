from email import message
import random
import requests
import json
import config as cfg
import main as main
import os
import time
import csv
import telebot

with open('data/config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

bot = telebot.TeleBot(config['API_TOKEN'])

def symbols_post_text(text :str):
    text_href = text.replace(' ', '_')
    for item in range(0, 10):
        if item == 0:
            if len(text_href) == 0:
                return f"unnamed_{time.time()}"
            else:
                result = text_href[item]
        else:
            result = result + text_href[item]
    return result


def vk_parser():

    with open('data/all_time.text', 'r') as file:
        all_time = file.read()

    with open('data/sleep.text', 'r') as file:
        sleep_time = file.read()

    with open('data/domain.csv', "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        domains = list(headers)

    
    for x in range(0, int(all_time) // int(sleep_time)):
        offset_rand = random.randint(0, 150)
        post_rand = random.randint(0, 2)
        rand_domain = random.choice(domains)
        
        qwe = ''
        text = ''

        responce = requests.get('https://api.vk.com/method/wall.get', params={
            "access_token": cfg.TOKEN_VK,
            "v": cfg.v,
            "domain": rand_domain,
            "offset": offset_rand
        })
        data = responce.json()

        try:
            text = data['response']['items'][post_rand]['text']
            text_href = symbols_post_text(text)
        except Exception:
            text = 'Такой группы нет'
            pass
        for it in range(0, len(data['response']['items'][post_rand]['attachments'])):
            try:
                qwe = data['response']['items'][post_rand]['attachments'][it]['photo']['sizes'][-1]['url']
            except Exception:
                print("Какая-то ошибка. Хз, что это...")
                vk_parser()
            img_data = requests.get(qwe).content
            if not os.path.exists(f"post/{text_href}"):
                os.makedirs(f"post/{text_href}", mode=0o777, exist_ok=True)
            with open(f"post/{text_href}/img_post_{it}.jpeg", 'wb') as file:
                file.write(img_data)

            with open(f"post/{text_href}/post_text.text", "w", encoding="utf-8") as file:
                file.write(text)

            bot.send_photo('@lamourdeglamour', img_data, text)
            time.sleep(5000)
