from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I 蕦杀 **{bn}** !!
I 森蓸t 拼o蕥 p森蕦拼 杀蕥s嫂c 嫂艐 拼o蕥蕗 蕸蕗o蕥p's vo嫂c蓸 c蕼蕦t 馃槈
T蕼蓸 co杀杀蕦艐蓷s I c蕥蕗蕗蓸艐t森拼 s蕥ppo蕗t 蕦蕗蓸:
鉁岎煆� /play - __P森蕦拼s t蕼蓸 蕗蓸p森嫂蓸蓷 蕦蕥蓷嫂o 蕟嫂森蓸 o蕗 Yo蕥T蕥蓳蓸 v嫂蓷蓸o t蕼蕗o蕥蕸蕼 森嫂艐母.__
鉁岎煆� /pause - __P蕦蕥s蓸 Vo嫂c蓸 C蕼蕦t M蕥s嫂c.__
鉁岎煆� /resume - __R蓸s蕥杀蓸 Vo嫂c蓸 C蕼蕦t M蕥s嫂c.__
鉁岎煆� /skip - __S母嫂ps t蕼蓸 c蕥蕗蕗蓸艐t M蕥s嫂c P森蕦拼嫂艐蕸 I艐 Vo嫂c蓸 C蕼蕦t.__
鉁岎煆伙笍 /stop - __C森蓸蕦蕗s T蕼蓸 Q蕥蓸蕥蓸 蕦s w蓸森森 蕦s 蓸艐蓷s Vo嫂c蓸 C蕼蕦t M蕥s嫂c.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "O蠅畏蓹r 馃挰", url="https://t.me/Mr_Nitric"
                    ),
                    InlineKeyboardButton(
                        "Source Cod蓹 馃摚", url="https://github.com/mrnitric/musicrobo"
                    )
                ]
            ]
        )
    )
