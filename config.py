"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  ZauteKm <https://telegram.dog/ZauteKm>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://live.rockfm.ro/rockfm.aacp")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '973861411')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '7378520'))
    CHAT = int(os.environ.get("CHAT", "-490005147"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-490005147")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "LGXZSK-DSRQMC-HCJVVZ-JIPVEL-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 120))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "6e04739d66a87f305207247d39875887")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1920790228:AAF0PFC4_HrbaMuPgUWrFD20GEpi0xwPsjg") 
    SESSION = os.environ.get("SESSION_STRING", "BAC1roB8z8C3Tjaj5HKohpJvVl0q7COw_5fYS4Df5zSsCzymEO-E7XHUDn7V7aDxqkyTsyAzoYFmLSqpteERvvMRMw7ItcLb9AzeXTyS6ZgdzS4hm1rHoyWQlmUdCGTd4oo5x5pArk50xymUEuflZ9h7PFidptMsfC4Sp6b8yLqTlILAEN1ZEzWStp3U0XHyzkcAUbCTyGjB5s6RV1uQdvQvNxWMj-w5dbq9x-qfF2O3czAVICJo2gGd29KvNaJ6kzX46nbayw4l5HIlEj0Aiply5PvShcysFzVVO9MdPSEzAyHyktdvCMAZkK2RYLATlB9hSuUQEZmKKdHNfjBcp7OqaFaYTQA")
    playlist=[]
    msg = {}
