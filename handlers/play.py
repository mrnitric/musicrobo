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
                f"**{bn} :-** 馃槙 V嫂蓷蓸os 森o艐蕸蓸蕗 t蕼蕦艐 {DURATION_LIMIT} 杀嫂艐蕥t蓸(s) 蕦蕗蓸艐't 蕦森森ow蓸蓷 !\n馃 T蕼蓸 p蕗ov嫂蓷蓸蓷 v嫂蓷蓸o 嫂s {audio.duration / 60} 杀嫂艐蕥t蓸(s)"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await message.reply_text(f"**{bn} :-** 馃檮 Yo蕥 蓷嫂蓷 艐ot 蕸嫂v蓸 杀蓸 蕦艐拼t蕼嫂艐蕸 to p森蕦拼 !")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{bn} :-** 馃槈 Q蕥蓸蕥蓸蓷 蕦t pos嫂t嫂o艐 #{await callsmusic.queues.put(message.chat.id, file_path=file_path)} !")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_text(f"**{bn} :-** 馃コ P森蕦拼嫂艐蕸...")
