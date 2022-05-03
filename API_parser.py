import requests
import json
import pandas as pd
response = requests.get('https://rss.applemarketingtools.com/api/v2/ru/apps/top-paid/100/apps.json')
response.status_code
data = response.content.decode()

dictionary = {} # создаю пустой словарь, в который я буду собирать данные
json_response = json.loads(data) # конвертирую результат запроса в объект Python, в данном случае словарь
for i in json_response['feed']:
    if i == 'results': # Собираю все, что находится в ключе results'
        for j in json_response['feed'][i]:
            for key in j:
                if key != 'url':
                    if type(j[key])!= list: # значание жанр представляет собой список, который надо распаковать
                        dictionary[key] = dictionary.get(key, []) + [j[key]]
                    else:
                        if len((j[key])) == 0:
                            dictionary[key] = dictionary.get(key, []) + ['-']
                        else:
                            dictionary[key] = dictionary.get(key, []) + [j[key][0]['name']]


df = pd.DataFrame(dictionary) # Создаю из словаря таблицу.
df.to_excel('parsing_1.xlsx') # Записываю таблицу в excel