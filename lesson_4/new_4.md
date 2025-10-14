# REST API 

REST (Representational State Transfer) - это архитектурный стиль, набор принципов взаимодействия компонентов ве бприложения в сети

## 5 принципов REST:

- Клиент-серверная архитектура
- Stateless (сервер не хранит состояние между запросами, каждый запрос должен содержать всю информацию для его обработки)
- Кэширование (кэширование ресурсов для быстродействия)
- Единый стиль (соотвестиве семантики http метода смыслу запроса, единый URL для одинковых сущностей, формат входных и выходных данных и др.)
- Многоуровневая система (клиента не должен волновать внутреннее устройство сервера)


# Pydantic
Работа с `dataclass` из одноименного модуля представляет некоторую проблему, она не контролирует передаваемые типы + некоторые типы могут быть не представимы ввиде *json* формате. На помощь пиходит **Pydantic**

## Основные функции 

- `model_dump_json` - перевод в `json`
    - `model_dump` - перевод в *словарь python*
- `model_validete_json` - перевод из `json`

```Python
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    birthdate: datetime
Me_to_json = User(id = 18, name = 'Max', birthdate = datetime(2007, 8, 4)).model_dump()
print(Me_to_json)

backwards = User.model_validate_json("{'id': 18, 'name': 'Max', 'birthdate': datetime.datetime(2007, 8, 4, 0, 0)}")
print(backwards)
```

# FAST API





