*Линтеры* - алгоритмы проходящие код перед запуском или перед комитом в гит
*Инкапсуляция* - сокрытие некоторой логики, которая не нужна пользователю (протектет)
*Полиморфичность* - свой-во функции, которая позволяет взаимодействовать с разными классами одинково

# using lambda function
```Python
b = [1, 2, 3, 4, 5]
s = list(map(lambda x: x ** 2, b))
print(s)
```

# Dataclass
- Декоратор, который автоматически проставляет и создает def __init__(переданные аргументы)

```Python
from dataclasses import dataclass
@dataclass
class User:
    id: int
    name: str
    balance: int

    def has_money(self) -> bool:
        return self.balance > 0
```

# Декораторы
Функция, которая изменяет какую-то другую функцию

```Python
count = 0 # Посчитать сколько раз использовалась функция hello
def hello(name: str) -> str:
    global count
    coutn += 1
    print(count)
    return f'Hi {name}!'
print(hello('World'))

def counter(f):
    count = 0
    def decorated(name):
        nonlocal count # для независимого каждого запуска декоратора
        count += 1
        print(count)
        return f(name)
    return decorated

def hello(name: str) -> str:
    return f'Bye, {name} !'

hello_countered = counter(hello('Max'))

@counter
def hello(name: str) -> str:
    return f'Hi, {name}!'

import time

def timer(f):
    def decorated(name):
        t0 = time.monotonic()
        v = f(name)
        print(f'Times to complete {time.monotonic() - t0}s')
        return v
    return decorated

@timer
def hello(name: str) -> str:
    time.sleep(3)
    return f'Bye, {name}!'

print(hello('Max'))
```
# Статический метод
@staticmethod - не принимает никаких self и не требовать экземпляра какого-то класса

@classmethod - можно использовать метод с аргументом класс