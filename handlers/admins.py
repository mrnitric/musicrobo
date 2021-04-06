from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text(f"**{BN} :-** 馃檮 Not蕼嫂艐蕸 嫂s p森蕦拼嫂艐蕸 !")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 馃 M蕥s嫂c P蕦蕥s蓸蓷 !")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text(f"**{BN} :-** 馃檮 Not蕼嫂艐蕸 嫂s P蕦蕥s蓸蓷 !")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 馃コ M蕥s嫂c R蓸s蕥杀蓸蓷 !")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** 馃檮 Not蕼嫂艐蕸 嫂s st蕗蓸蕦杀嫂艐蕸 !")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**{BN} :-** 鉂� St蕗蓸蕦杀嫂艐蕸 Stopp蓸蓷 !")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** 馃檮 Not蕼嫂艐蕸 嫂s p森蕦拼嫂艐蕸 to s母嫂p !")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file_path"]
            )

        await message.reply_text(f"**{BN} :-** 馃槵 S母嫂pp蓸蓷 t蕼蓸 c蕥蕗蕗蓸艐t so艐蕸 !")
