import re
import asyncio
import requests
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_ip_info(ip_address):
    url = f'http://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    data = response.json()
    return data


def is_valid_ip(ip):
    ip_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if re.match(ip_pattern, ip):
        octets = ip.split('.')
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False
        return True
    else:
        return False


def is_valid_data(ip):
    ip_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(ip_regex, ip) is not None


@dp.message(Command("start"))
async def start_func(message: types.Message):
    logger.info(f"User {message.from_user.id} started the bot")
    await message.answer("Напишите IP-адрес и узнайте информацию")


@dp.message()
async def info_ip(message: types.Message):
    logger.info(f"Received message from user {message.from_user.id}: {message.text}")
    if not is_valid_ip(message.text):
        await message.answer("Напишите IP-адрес")
        logger.warning(f"Invalid IP address provided by user {message.from_user.id}")
        return
    else:
        info = get_ip_info(message.text)
        for key, value in info.items():
            if key == 'loc':
                lat, lon = value.split(',')
                map_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
                await message.answer(f"{key}: <a href='{map_link}'>{value}</a>", parse_mode=ParseMode.HTML)
            elif key != 'readme':
                if key == 'ip' and is_valid_data(value):
                    await message.answer(f"{key}: {value}")
                else:
                    await message.answer(f"{key}: {value}")
    logger.info(f"Sent IP information to user {message.from_user.id}")


async def main():
    logger.info("Bot started")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
