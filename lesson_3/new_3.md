# Импорт библиотек
встроенные
установленные
локальные

# UDP and TCP
два самых популряных протокола на транспортном уровне
TCP - гарантирует, что пакет долетел в нужном порядке (игры и тд)
UDP - не гарантирует, что пакет далетит (трансляция и тд)


```bash
curl -v https://edu.itatmisis.ru
```

HTTP - самый популярный протокол прикладного уровня
Простой текстовый протокол 
Код возврата
    2XX - хороший код возврата 
    3XX - Permanent Redirect - если запрос отправлен по http, то могут и перебросить на https
    4XX - client Error 
        401 - не зарегестрированны на сервере
        403 - попытка отправить запрос, на который нету прав
    5XX - Server Error 

# Популряные HTTP методы запросов

```bash
curl -X GET http://httpbin.org/
```

1. `OPTIONS` - доступные запросы
2. `GET` - получение ресурсов *
    - нельзя использовать метод `GET` и передовать что-то в теле запроса 
3. `POST` - создание ресурса *
4. `HEAD` - получение заголовка
5. `PUT` - обновление ресурса
6. `PATCH` - обновление части ресурса
7. `DELETE` - удаление ресурса 


# Подходы реализации запроса

HTTP - не стандартизирует вид ответа / запроса, на этой основе создаются 

1. **Path параметры** - внутри самого пути будет отображаться наши действия
    `https://animego.me/anime/filter/dubbing-is-anidub/apply`
    - `filer` - применение фильтра
    - `dubbing-is-anudub` - озвучка анидаб
    - `apply` - применить
2. **Qwery параметры** 
    `https://www.google.com/search?q=what+is+http`
    - `?` - начало qwery строки 


# JSON (JavaScript Object Notation)
- способ представления объектов на java scripte

1. `dumps` - передать что-то в *json* формат
```python
import json
a = {'Russian': 'Moscow'}
print(json.dumps(a)) # дампинг json в string формат
```

2. `loads` - получить что-то из *json* формата

```python
import json
data = json.loads('["key1", 123, null]')
```

## Перевод ответа в *json* формат

```python
import requests
r = requests.get('https://httpbin.org/get')
print(r.json()) # встроенный метод в requests, который сразу переведет response в jsons формат и даст взаимодействие словарям в python
```


