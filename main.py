import asyncio
import logging

import telebot
from telebot import types, util
from telebot.async_telebot import AsyncTeleBot
from telebot.types import User

from env import TELEGRAM_BOT_AUTH_TOKEN, TELEGRAM_INSPECTOR_CHANNEL, IS_DEBUG

logger = telebot.logger
telebot.logger.setLevel(
    logging.DEBUG if IS_DEBUG else logging.INFO
)

bot = AsyncTeleBot(TELEGRAM_BOT_AUTH_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    # logger.log('{name} start chat with the bot'.format(name=format_user_name(message.from_user)))

    await bot.reply_to(message, 'Hi and Bye!')


@bot.chat_member_handler()
async def chat_m(message: types.ChatMemberUpdated):
    chat_id = message.chat.id if message.chat is not None else 0
    new = message.new_chat_member

    if new.status == "member" and chat_id == int(TELEGRAM_INSPECTOR_CHANNEL):
        user_name = format_user_name(new.user)
        is_admin = new.can_manage_chat if new.can_manage_chat is not None else False

        logger.info('%s joined on the channel', user_name)

        if not is_admin:
            # Kick member
            await bot.ban_chat_member(message.chat.id, new.user.id, revoke_messages=False)
            logger.info('%s was kicked from the channel', user_name)

            # UnBan member
            await bot.unban_chat_member(message.chat.id, new.user.id)
            logger.info('%s was unbanned on the channel', user_name)

        else:
            logger.info('%s is admin and still place on the channel', user_name)


def format_user_name(user: User):
    return f'{user.first_name} {user.last_name}, username: @{user.username}'


asyncio.run(
    bot.polling(allowed_updates=util.update_types)
)
