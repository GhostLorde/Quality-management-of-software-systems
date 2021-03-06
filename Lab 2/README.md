Лабораторная работа №2 Зорихина М. ПИ20-2
-------------------------------------------
Предусловия: 
1. Созданный примитивный файловый менеджер.
2. Программа должна работать в определенной папке (рабочей папки менеджера) и позволять пользователю выполнять следующие простые действия в пределах рабочей папки:
* Создание папки (с указанием имени)
* Удаление папки по имени;
* Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
* Создание пустых файлов с указанием имени;
* Запись текста в файл;
* Просмотр содержимого текстового файла;
* Удаление файлов по имени;
* Копирование файлов из одной папки в другую;
* Перемещение файлов;
* Переименование файлов.


Задание:
-----------
Необходимо написать тесты, которые проверяют работу файлового менеджера.
Покрытия тестами составляет от 80% 

Указания к выполнению
* Библиотека для тестирования Pytest
* Использовать технику позитивного и негативного тестирования
* Использовать технику граничных условий и классов эквивалентности
* Разработка должна вестись с использованием СКВ Git. Код должен публиковаться в репозитории на GitHub.
* Файл README.md должен содержать описание созданных тестов и скриншот с отчетом о запуски и прохождением тестов.

Настраиваю PyCharm для работы с Pytest
<img width="1432" alt="Снимок экрана 2021-12-19 в 15 44 29" src="https://user-images.githubusercontent.com/90088355/146678644-2dca7304-54a9-4ba5-9f33-5aaca03936ca.png">

Код файлового менеджера и код с тестом в файлах выше. 

Тестирование будет производиться с использованем фикстур , а также тестами этих фикстур. @pytest.fixture

В случае положительного прохождения теста, возвращается значение True, которое сравнивается с предустановленным значением. 




Результат тестирования pytest:
<img width="904" alt="Снимок экрана 2021-12-19 в 18 39 45" src="https://user-images.githubusercontent.com/90088355/146681121-6434e182-8185-46b2-88c7-67080a31baf0.png">

.pytast_cashe - созданная библиотекой директория с лог файлами.


<img width="273" alt="Снимок экрана 2021-12-19 в 18 41 53" src="https://user-images.githubusercontent.com/90088355/146681165-4b7bfc81-d5f7-4579-b4f4-cfc39251466c.png">

Описание всех тестов в проекте:

<img width="450" alt="Снимок экрана 2021-12-19 в 18 43 00" src="https://user-images.githubusercontent.com/90088355/146681185-98400e33-501a-4d2c-8753-046984cf2e1e.png">

Вывод - pytest оказался довольно удобным инструментом для тестирования. Удобство заключается в том, что его можно подстроить под любой тип программы. 
