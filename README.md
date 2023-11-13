# Сервис YaCut

## ОПИСАНИЕ
YaCut - это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### ОСОБЕННОСТИ
Реализация сервиса и API на Flask

### ЭНДПОИНТЫ
| Маршрут | HTTP методы | Описание |
|:---|:---|:---|
| `/api/id/` | `POST` | создание новой короткой ссылки |
| `/api/id/<short_id>/` | `GET` | получение оригинальной ссылки по указанному короткому идентификатору |

## ЗАПУСК ПРОЕКТА
1. Клонировать репозиторий
```
git clone git@github.com:monteg179/yacut.git
cd yacut
```
2. Создать и настроить виртуальное окружение
```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
3. Создать базу данных
```
flask db upgrade
```
4. Запуск dev-сервера.
```
python -m yacut
```
После запуска сервис будет доступен по адресу http://localhost:5000

## ИСПОЛЬЗОВАНИЕ

### создание короткой ссылки автоматически 
- запрос
```
POST http://localhost:5000/api/id/ HTTP/1.1
content-type: application/json
{
    "url": "https://peps.python.org/pep-0008/"
}
```
- ответ
```
HTTP/1.0 201 CREATED
Content-Type: application/json
{
  "short_link": "http://localhost:5000/zhXCxX",
  "url": "https://peps.python.org/pep-0008/"
}
```
### создание короткой ссылки 
- запрос
```
POST http://localhost:5000/api/id/ HTTP/1.1
content-type: application/json
{
    "url": "https://peps.python.org/pep-0008/"
    "custom_id": "pep8"
}
```
- ответ
```
HTTP/1.0 201 CREATED
Content-Type: application/json
{
  "short_link": "http://localhost:5000/pep8",
  "url": "https://peps.python.org/pep-0008/"
}
```
### получение оригинальной ссылки
- запрос
```
GET {{server}}/api/id/pep8/ HTTP/1.1
```
- ответ
```
HTTP/1.0 200 OK
Content-Type: application/json
{
  "url": "https://peps.python.org/pep-0008/"
}
```


## ТЕХНОЛОГИИ
- Python 3.9
- Flask
- SQLAlchemy

## АВТОРЫ
* Сергей Кузнецов - monteg179@yandex.ru
