from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I ʌɱ **{bn}** !!
I ɭɘt ƴoʋ pɭʌƴ ɱʋsɩc ɩŋ ƴoʋʀ ʛʀoʋp's voɩcɘ cʜʌt 😉
Tʜɘ coɱɱʌŋɗs I cʋʀʀɘŋtɭƴ sʋppoʀt ʌʀɘ:
✌🏻 /play - __Pɭʌƴs tʜɘ ʀɘpɭɩɘɗ ʌʋɗɩo ʆɩɭɘ oʀ YoʋTʋɓɘ vɩɗɘo tʜʀoʋʛʜ ɭɩŋĸ.__
✌🏻 /pause - __Pʌʋsɘ Voɩcɘ Cʜʌt Mʋsɩc.__
✌🏻 /resume - __Rɘsʋɱɘ Voɩcɘ Cʜʌt Mʋsɩc.__
✌🏻 /skip - __Sĸɩps tʜɘ cʋʀʀɘŋt Mʋsɩc Pɭʌƴɩŋʛ Iŋ Voɩcɘ Cʜʌt.__
✌🏻️ /stop - __Cɭɘʌʀs Tʜɘ Qʋɘʋɘ ʌs wɘɭɭ ʌs ɘŋɗs Voɩcɘ Cʜʌt Mʋsɩc.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oωηər 💬", url="https://t.me/Mr_Nitric"
                    ),
                    InlineKeyboardButton(
                        "Source Codə 📣", url="https://github.com/mrnitric/musicrobo"
                    )
                ]
            ]
        )
    )
