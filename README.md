
<h1 align="center">Test Work For Nova</h1>

<h2 align="center"> Тестовое задание </h2>

<div align="center">
    
<div>
    <a href="https://pypi.org/project/gunicorn/"><img alt="Static Badge" src="https://img.shields.io/badge/gunicorn-21.2.0-darkgreen?labelColor=gray"></a>
</div>
<div>
    <a href="https://www.python.org/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python"/></a>
    <a href="https://www.djangoproject.com/"><img width="48" height="48" src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="python"/></a>
    <a href="https://www.nginx.com/"><img width="48" height="48" src="https://img.icons8.com/color/48/nginx.png" alt="python"/></a>

</div>

</div>

___

<h2>1. Установка</h2>

1.1 Клонируйте проект:
    
```bash
    git clone git@github.com:AndrewDyakonow/TestWorkNOVA.git
```

1.2 Создайте и активируйте виртуальное окружение.
```bash
    python3 -m venv venv
    source venv/bin/activate
```
1.3 Установите зависимости.
```bash
    pip install -r requirements.txt
```

1.4 Примените миграции
```bash
    python3 manage.py migrate
```

1.5 Запустите тестовый сервер
```bash
    python3 manage.py runserver
```

___

<h2>2. Работа</h2>

2.1 Приложение крутится на сервере и доступно по адресу http://34.105.53.149/.

2.2 Реализован эндпоинт для создания Google документа на Google Drive.

Для создания документа необходимо выполнить POST запрос по адресу ``http://34.105.53.149/``.
В теле запроса необходимо передать параметры "data" - тело документа и "name" - название документа
```text
{
    "data": str,
    "name": str,
}
```

2.3 Также имеется эндпоинт для удаления всех файлов на гугл диске.

Для удаления, необходимо выполнить DELETE запрос по адресу ``http://34.105.53.149/delete/``



<h2>3. Комментарий</h2>
    
Имеет смысл обратить внимание на то, что объект ``googleAPI``, имеет метод ``show_file_list`` 
и служит для получения списка всех документов на Google Drive