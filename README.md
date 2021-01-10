# Multi-user Flask Event App (Event scheduling service) / Многопользовательский сервис планирования событий

    Flask, PostgreSQL, Docker, Heroku

Описание:

    Multi-user Flask Event App - сервис который поддерживает работу нескольких пользователей. 
    Пользователи могут создавать событие, которое доступно остальным пользователям.
    У каждого события есть следующие параметры: автор, время начала, время конца, тема и описание.
    Каждый пользователь может просматривать все события, которые созданы любыми пользователями.
    Каждый пользователь может редактировать, удалять и создавать события, где пользователем является он.
    Реализована страница, на которой есть общий вид всех событий.
    
Проект также размещен на Heroku: https://fierce-castle-71702.herokuapp.com/

Разворачиваем проект локально:

1. Способ 1 (с использованием SQLite3):

- Скачайте репозиторий

- Создайт виртуальное окружение:

      python -m venv env

- Активируйте виртуальное окружение:

      source env/bin/activate
      
- Чтобы установить все требуемые библиотеки python в новом окружении выполните команду:

      pip install -r requirements.txt
  
  Если у вас macOS до выполнения команды pip install -r requirements.txt выполните команду:

      env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2==2.8.4      
      
Для предотвращения появления ошибки (error: command 'gcc' failed with exit status 1.) при установке зависимостей.

- Запустите сервер командой:

      python -m flask run

- Приложение будет доступно по пути: http://127.0.0.1:5000/

2. Способ 2 (с использованием PostgreSQL через docker-compose):

- Перед запуском контейнера, по возможности следует удалить все образы и контейнеры использующие postgres на вашем компьютере, чтобы предотвратить возникновение ошибок.

- Запустите команду:

      docker-compose up

- Приложение будет доступно по пути: http://0.0.0.0:5000/

