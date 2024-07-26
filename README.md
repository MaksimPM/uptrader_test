<h1 align="center">UpTraderTest</a> 
<h2 align="left">Для запуска проекта необходимо:</h2>
  
• Установить виртуальное окружение в корневой папке проекта командой:
```shell
python -m venv venv
```

• Создать в корне проекта файл ```.env``` и заполнить данные по образцу из файла ```.env.sample```

• Установить все необходимые зависимости, указанные в файле ```requirements.txt```:
```shell
pip install -r requirements.txt
```
• Выполнить создание и применение миграций командами:
```shell
python3 manage.py makemigration
```
```shell
python3 manage.py migrate
```
   
• Создать суперпользователя командой:
```shell
python3 manage.py csu
```

• Запустить сервер командой:
```shell
python3 manage.py runserver
```

<h2 align="left">Для запуска проекта через Docker необходимо:</h2>

• Запустить Docker командой:
```shell
docker compose up --build
```

<h2 align="left">Логика работы:</h2>
<h3 align="left">Создание и редактирование меню:</h3>
• Администратор добавляет новые пункты меню или редактирует существующие через админку Django.

• При добавлении или редактировании пункта меню администратор также может указать его родительский пункт для создания иерархии меню.
<h3 align="left">Отображение меню на веб-странице:</h3>
  
• Используйте тег в шаблоне следующим образом: ```{% draw_menu "main_menu" %}```. На месте ```"main_menu"``` вы указываете название меню, которое хотите отобразить. Можно выводить любое меню в любом месте и количестве. 
