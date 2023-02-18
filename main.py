import requests
import json
import time

# библиотека красивого вывода pprint
from pprint import pprint

import CONST


def answer_user_bot(data):
    url = CONST.URL.format(TOKEN=CONST.TOKEN, method=CONST.SEND_METH)
    response = requests.post(url, data={"chat_id": CONST.MY_ID, "text": data})
    if response.status_code != 200:
        return False
    return True

def parse_weather(data):
    # используем цикл для подстраховки, вдруг там нет таких ключей или еще что-то неясное
    for elem in data['weather']:
        weather_state = elem['main']
    # weather_state = data['weather'][0]['main'] - вариант без защиты, т.к. список может быть значений(хз)
    temp = data['main']['temp']
    city = data['name']
    msg = f"The weather in the {city}. Temp is {temp}, and the state is {weather_state}"
    return msg

def get_weather(location):
    url = CONST.WEATHER_URL.format(CITY=location, WEATHER_TOKEN=CONST.WEATHER_TOKEN)
    response = requests.get(url)
    data = json.loads(response.content)
    if response.status_code != 200:
        return "city is not found"

    return parse_weather(data)

def get_message(data):
    return data['message']['text']


def save_update_id(update):
    pprint(update)
    with open(CONST.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    CONST.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = CONST.URL.format(TOKEN=CONST.TOKEN, method=CONST.UPDATE_METH)
        content = requests.get(url).text
        data = json.loads(content)
        # существует 2 способа полученния данных с словаря data.get('ключ') и по ключу data['ключ']
        # лучший вариант по гет data.get('ключ'), т.к. если значения нет (None), ошибку не вернет, а по ключу вернет

        # ставим риверс(обратный порядок), чтобы к последней паре в словаре обратится как первой, [::-1] - риверс
        result = data['result'][::-1]  # сортировка в обратном порядке
        for elem in result:
            if elem['message']['chat']['id'] == CONST.MY_ID:
                needed_part = elem
                break

        if CONST.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            weather = get_weather(message)
            answer_user_bot(weather)
            save_update_id(needed_part)



        # pprint(data)
        #break
        time.sleep(2)


if __name__ == "__main__":
    main()
