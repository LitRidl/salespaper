# Доска объявлений о купле-продаже
Доска структурированных объявлений с возможностью поиска по характеристкам.

## Инструкция
1. git clone git@github.com:LitRidl/salespaper.git
2. При необходимости установить Python 2.7 и связанные утилиты:
  1. sudo apt-get install python-setuptools python-dev build-essential
  2. sudo easy_install pip
  3. sudo pip install virtualenv
3. Перейти в директорию проекта (cd salespaper)
4. Создать виртуальное окружение: virtualenv -p python2.7 ENV
5. Активировать виртуальное окружение: . ENV/bin/activate
6. Разрешить python-зависимости: pip install dependencies.txt
7. Подготовить БД
  1. Запустить консоль администратора python shell.py
  2. Командой db.create_all() создать БД
  3. Командой create_user('ipetrov', '123456', 'ipetrov98@gmail.com', 'admin') создать пользователя-администратора
8. Запустить сервер: python run.py
9. Перейти в браузере по адресу http://localhost:5000/

## Исходная постановка задачи
Сайт купли-продажи авто:
- возможность размещать объявления о продаже авто с некими характеристиками - достатоно взять 4-5 характеристик
- управление-модерирование (CRUD) всеми объявлениями в админке
- иерархия доступа к объявлениям - зарегистрированный пользователь может редактировать только свои объявления.
- поиск авто по неким фильтрам, напр, год выпуска, КПП и пр


## Функциональность
- размещение пользователем объявлений о продаже авто с указанием числовых и ординальных характеристик.
- возможность регистрации и входа/выхода пользователя.
- из профиля можно управлять своими объявлениями.
- объявления можно просматривать по отдельности и массово в ленте.
- объявления в ленте можно фильтровать по характеристикам.
- разделение зарегистрированных пользователей на простых и администраторов.
- пользователь может создавать, изменять и закрывать свои объявления.
- администратор дополнительно может удалять, изменять и блокировать чужие объявления.
- администратор может блокировать других пользователей и просматривать их профили.
