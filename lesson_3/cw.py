import requests

# Простой запрос в гугл
r = requests.get('https://www.google.com/', params = {
    'q': 'Python for 5 minuts'
})

# Запрос с header-ом
r = requests.get('https://www.google.com/', params = {
    'q': 'Python for 5 minurts',
    'headers': 'application/json'
})
print(r.status_code)

# Перевод в json
import json
a = {'Russian': 'Moscow', 'USA': "Washington"}
# Нужно передать в каком-то виде HTTP словарь выше
print(json.dumps(a))

# Перевод из json
data = json.loads('["key1", 123, null]')
print(data)

# Получение ответа в json и перевод в python словарь
r = requests.get('https://httpbin.org/get')
print(r.json()['args'])

# 

