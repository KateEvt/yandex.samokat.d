﻿# Тесты на проверку получения заказа по номеру трека заказа 
- Для запуска тестов должны быть установлены пакеты pytest и requests

# Шаги автотеста:

- Выполнить запрос на создание заказа.
- Сохранить номер трека заказа.
- Выполнить запрос на получения заказа по треку заказа.
- Проверить, что код ответа равен 200.