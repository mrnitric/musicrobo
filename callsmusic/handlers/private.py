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

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I ʌɱ ʌŋ opɘŋ-soʋʀcɘ @Music_Rob_Bot ɓot, I ɭɘt ƴoʋ pɭʌƴ ɱʋsɩc ɩŋ ƴoʋʀ ʛʀoʋp’s voɩcɘ cʜʌt.

Tʜɘ coɱɱʌŋɗs I cʋʀʀɘŋtɭƴ sʋppoʀt ʌʀɘ:

🤞 /play - pɭʌƴ tʜɘ ʀɘpɭɩɘɗ ʌʋɗɩo ʆɩɭɘ oʀ YoʋTʋɓɘ vɩɗɘo
🤞 /pause - pʌʋsɘ tʜɘ ʌʋɗɩo stʀɘʌɱ
🤞 /resume - ʀɘsʋɱɘ tʜɘ ʌʋɗɩo stʀɘʌɱ
🤞 /skip - sĸɩp tʜɘ cʋʀʀɘŋt ʌʋɗɩo stʀɘʌɱ
🤞 /stop - cɭɘʌʀ tʜɘ qʋɘʋɘ ʌŋɗ ʀɘɱovɘ tʜɘ ʋsɘʀɓot ʆʀoɱ tʜɘ cʌɭɭ
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Soυrcə Codə", url="https://github.com/mrnitric/music-robo"
                    ),
                    InlineKeyboardButton(
                        "Oωηer", url="https://t.me/mr_nitric"
                    )
                ]
            ]
        )
    )
