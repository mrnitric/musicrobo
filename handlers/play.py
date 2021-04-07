from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

import callsmusic

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name


@Client.on_message(command("play") & other_filters)
@errors
async def play(_, message: Message):
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**{bn} :-** 😕 Vɩɗɘos ɭoŋʛɘʀ tʜʌŋ {DURATION_LIMIT} ɱɩŋʋtɘ(s) ʌʀɘŋ't ʌɭɭowɘɗ !\n🤐 Tʜɘ pʀovɩɗɘɗ vɩɗɘo ɩs {audio.duration / 60} ɱɩŋʋtɘ(s)"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await message.reply_text(f"**{bn} :-** 🙄 Yoʋ ɗɩɗ ŋot ʛɩvɘ ɱɘ ʌŋƴtʜɩŋʛ to pɭʌƴ !")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{bn} :-** 😉 Qʋɘʋɘɗ ʌt posɩtɩoŋ #{await callsmusic.queues.put(message.chat.id, file_path=file_path)} !")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_text(f"**{bn} :-** 🥳 Pɭʌƴɩŋʛ...")
