# Calls Music 2 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from ..callsmusic import callsmusic
from ..helpers.filters import command, other_filters
from ..helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == "paused"
    ):
        await message.reply_text("🙄 Notʜɩŋʛ ɩs pɭʌƴɩŋʛ !")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("😐 Mʋsɩc Pʌʋsɘɗ !")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == "playing"
    ):
        await message.reply_text("🙄 Notʜɩŋʛ ɩs Pʌʋsɘɗ !")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("😐 Mʋsɩc Rɘsʋɱɘɗ !")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("🙄 Notʜɩŋʛ ɩs Stʀɘʌɱɩŋʛ !")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("😐 Stoppɘɗ Stʀɘʌɱɩŋʛ !")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("🙄 Notʜɩŋʛ ɩs pɭʌƴɩŋʛ to sĸɩp !")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file_path"]
            )

        await message.reply_text("🙄 Sĸɩppɘɗ tʜɘ cʋʀʀɘŋt soŋʛ !")
