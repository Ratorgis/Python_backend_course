from fastapi import FastAPI


# Использование Curlify - перевода http запросы в понятный и подробный curl
from curlify2 import Curlify
import requests

resp = requests.get("https://google.com")
Curlify(resp.request).to_curl()


# Тестировака через TestClient
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/hello")
def hell() -> str:
    return "word"

client = TestClient(app)
response = client.get("/hello")
assert response.status_code == 200
assert response.text == '"word"'


# Использование Хэдеров
from fastapi import Header
app = FastAPI()
@app.get("/hello")
def hello(user_name: str = Header(...)) -> str:
    return f"Hello {user_name}"
clinet = TestClient()
response = client.get("/hello", headers = {"User-Name": "Olya"})
assert response.status_code == 200 
assert response.text == '"Hello Olya"'


# Логеры и Loguru разделение на уровни логирования
from loguru import logger

logger.debug('Когда происходит что-то не очень важное')
logger.info('Когда происходит что-то важное')
logger.warning('Когда происходит не совсем ошибка, но и не стандартное поведенеи')
logger.error('когда происходит ошибка')

# Уникальность логера - работа может продолжится дальше, но ошибка будет залогированна

try: 
    1 / 0
except Exception:
    logger.exception('exception.raised')
print('Hi')


# Мидлвары - функции, которые выполняются до и после запросов
# могут отфильтровать запросы, логировать их
# Мидл вар находится может обработать Request или же Response

import time
from fastapi import Request, Response

@app.middleware('http')
async def add_process_time_header(request: Request, call_next) -> Response:
    t0 = time.time()

    response: Response = await call_next(request)

    elapse_ms = round((time.time() - t0) * 1000, 2)
    response.headers['X-Process-Time'] = str(elapse_ms)
    logger.debug("{} {} done in {}ms", request.method, request.url, elapse_ms)

    return response





