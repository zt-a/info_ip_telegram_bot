# Info IP Telegram Bot

Info IP Telegram Bot - это Telegram бот, который предоставляет информацию об IP-адресе, включая географические координаты и ссылку на карту.

## Описание

Этот бот разработан на Python с использованием библиотеки aiogram для работы с Telegram API. Он позволяет пользователям отправлять IP-адреса и получать информацию о них, включая географические координаты и ссылку на карту Google Maps.

## Функции

- Получение информации об IP-адресе: бот принимает IP-адрес от пользователя и возвращает информацию о нем, включая географические координаты и ссылку на карту Google Maps.
- Проверка валидности IP-адреса: перед запросом информации бот проверяет введенный IP-адрес на корректность.
- Использование HTML разметки: для вывода информации о географических координатах бот использует HTML разметку, чтобы вставить ссылку на карту.

## Установка и запуск

### Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your_username/info_ip_telegram_bot.git
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Создать файл .env и внести необходимые изменения указав токен вашего бота на переменную **BOT_TOKEN**

### Запуск 

4. **Создайте файл службы для systemd (Linux)**:

    4.1. Скопируйте файл службы в системный каталог:

    ```bash
    sudo cp /home/ubuntu/info_ip_telegram_bot/info_ip_tg_bot.service /etc/systemd/system/
    ```

    4.2. Обновите конфигурацию systemd:

    ```bash
    sudo systemctl daemon-reload
    ```

    4.3 Включите службу:

    ```bash
    sudo systemctl enable info_ip_tg_bot.service
    ```

    4.5. Запустите службу:

    ```bash
    sudo systemctl start info_ip_tg_bot.service
    ```

    Проверьте статус службы:

    ```bash
    sudo systemctl status info_ip_tg_bot.service
    ```

    Если служба запущена и работает корректно, вы должны увидеть сообщение о ее статусе без ошибок.

## Файл службы для Windows

Для запуска вашего бота как службы в Windows используйте инструменты управления службами или PowerShell.

## Лицензия

Этот проект лицензируется по лицензии [MIT](LICENSE).

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной по адресу zt20061113@gmail.com.
