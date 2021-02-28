Для запуска требуется версия python 3.7.x
Каталог backend представляет серверную часть построеную на основе Flask
создайте новый проект указав каталог backend в качестве корня проекта.
Установите необходимые зависимости описанные в файле requirements.txt
В качестве базы данных используется postgresql и бэкэнд настроен на работу именно с ней.
После создания БД в файл backend/DataBaseController/DataBaseController.py задайте ваше имя пользователя БД и пароль:
</br>database_user_name = "postgres"
</br>database_user_pass = "XXXX"</br>
В файле backend/FlaskService/FlaskService.py задайте любой свободный порт.
По умолчанию сервер запуститься на порту 8000
И запустите проект.

Для frontend используется node.js и React, дополнительно потребуется установить библиотеку Bootstrap4 с помощью команды: </br>npm install --save bootstrap-4-react
