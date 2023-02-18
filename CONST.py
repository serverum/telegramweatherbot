# большими буквами обозначают константы
TOKEN = "PASTE YOUR TELEGRAM TOKEN HERE"

URL = "https://api.telegram.org/bot{TOKEN}/{method}"
MY_ID = YOUR_ID
UPDATE_ID_FILE_PATH = 'update_id'


file = open('update_id', 'w')
file.close()

import os.path

if not os.path.exists(UPDATE_ID_FILE_PATH):
    with open(UPDATE_ID_FILE_PATH, 'w') as file:
        file.write()
else:
    with open(UPDATE_ID_FILE_PATH, 'r') as file:
        data = file.readline()
        if data:
            data = int(data)
        UPDATE_ID = data


UPDATE_METH = "getUpdates"  # ф-я обновления статуса присланных сообщений и состояний
SEND_METH = "sendMessage"  # ф-я отправки сообщения в оф. апи от телеграм
SEND_DOC_METH = "sendDocument"  # отправка файлов, 2 обязательных аргумента, chat_id + дескриптор файла (через open())

#-------------------API OF THE WEATHER SERVICE https://openweathermap.org/current#name

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_TOKEN}&units=metric"
WEATHER_TOKEN = "YOUR_OPENWEATHERMAP_API_TOKEN"

