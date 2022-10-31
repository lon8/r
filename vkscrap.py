import random
import requests
import json
import config as cfg
import main as main
import os
import time
import csv

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
    offset_rand = random.randint(0, 150)
    post_rand = random.randint(0, 2)

    with open('data/domain.csv', "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        domains = list(headers)
        
    rand_domain = random.choice(domains)
    for rand_domain in len(domains):

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
        except Exception:
            text = ''
            pass
        text_href = symbols_post_text(text)
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
        
        print(1)

print("Закончили")