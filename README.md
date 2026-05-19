# telegram-crm-bot
Привіт всім. Я написав невеличкий бот, можливо комусь буде корисний. 

Бот створений для запису клієнтів і занесення їх в базу даних, також для зібрання відгуків і коментарів. 
Він записує номер телефону, коментар, ім'я, а також email.

Для роботи бота Вам потрібний буде Visual Studio, також встановлений Python, та налаштований .env для коректного запуску. 
## features
Він підтримує такі команди:

- /orders показує поточну Базу даних клієнтів, також додана можливість фільтрації, може показати лише певну кількість клієнтів. Приклад: /orders 2 покаже лише перших двох клієнтів прямо в боті. 

- /update надає можливість оновлювати базу даних, а саме коментарі(з часом буде додаватись функції)

- /delete надає можливість видаляти певних користувачів із БД Приклад: /delete 1 видалить користувача із ID 1.

Для запуску бота варто створити нового бота у BotFather в Телеграм, визначити його Токен, який ви отримаєте і також за допомогою UserInfo визначити ID людини яка буде адміністратором.
і вставити у ADMIN_ID свій ID.







					English
Hello everyone. I wrote a small bot, maybe someone will find it useful.

The bot is designed to record customers and enter them into the database, as well as to collect feedback and comments.
It records the phone number, comment, name, and email.

For the bot to work, you will need Visual Studio, also Python installed, and configured .env for correct launch.
## features
It supports the following commands:

- /orders shows the current Customer Database, also added the ability to filter, can show only a certain number of customers. Example: /orders 2 will show only the first two customers directly in the bot.

- /update provides the ability to update the database, namely comments (functions will be added over time)

- /delete provides the ability to delete specific users from the database Example: /delete 1 will delete the user with ID 1.

To start the bot, you should create a new bot in BotFather in Telegram, determine its Token, which you will receive, and also use UserInfo to determine the ID of the person who will be the administrator.
and insert your ID into ADMIN_ID.
