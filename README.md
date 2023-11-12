# YaCut

## ОПИСАНИЕ
YaCut - это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### ОСОБЕННОСТИ
Реализация backend и frontend на Flask

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
3. Выполнить миграции
```
flask db migrate
flask db upgrade
```
4. Запуск dev-сервера
```
flask run
```

## ИСПОЛЬЗОВАНИЕ

## ТЕХНОЛОГИИ
- Python 3.9
- Flask
- SQLAlchemy

## АВТОРЫ
* Сергей Кузнецов - monteg179@yandex.ru
