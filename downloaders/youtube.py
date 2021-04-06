from os import path

from youtube_dl import YoutubeDL

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"**{bn} :-** 馃槙 V嫂蓷蓸os 森o艐蕸蓸蕗 t蕼蕦艐, {DURATION_LIMIT} 杀嫂艐蕥t蓸(s) 蕦蕗蓸艐't 蕦森森ow蓸蓷, t蕼蓸 p蕗ov嫂蓷蓸蓷 v嫂蓷蓸o 嫂s {duration} 杀嫂艐蕥t蓸(s)"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
