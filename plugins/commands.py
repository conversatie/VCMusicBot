"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  Zaute Km | TGVCSETS

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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES, mp
from config import Config
import os
import sys
import subprocess
import asyncio
from signal import SIGINT
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Hello, [{}](tg://user?id={})\n\nRedau muzică 24×7 Radio/Music Player.\n\nApasă /help pentru mai multe detalii.</b>"
HELP = """
**<b>Muzică pe VoiceChat</b>:**

**<b>Comenzi membri</b>:**

▷/play **[nume melodie]/[yt link]**: ca răspuns unui fișier audio.
▷/dplay **[nume melodie]:** Redare muzică din Deezer.
▷/player:  Arată melodia în curs.
▷/help: Ajutor comenzi.
▷/playlist: Arată playlist-ul.

**<b>Comenzi Admini</b>:**
▷/skip: Omiteți melodia curentă sau /skip n(n= nr. meoldiei din playlist) 
▷/join: Alăturați-vă chatului vocal.
▷/leave: Părăsiți chatul vocal actual.
▷/vc: Verificați ce VC este asociat.
▷/stop: Opriți redarea.
▷/radio: Porniți Radio.
▷/stopradio: Oprește fluxul radio.
▷/replay: Redați de la început.
▷/clean: Eliminați fișierele RAW PCM neutilizate.
▷/pause: Întrerupeți redarea.
▷/resume: Reluați redarea.
▷/volume: Schimbați volumul (0-200).
▷/mute: Mute în VC.
▷/unmute: Activați redarea în VC.
▷/restart: Repornește botul. 
"""



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("🇷🇴România HUB", url='https://t.me/romaniahub'),
    ],
    [
        InlineKeyboardButton('👥 Grup', url='https://t.me/romuzicaro'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/iZaute/6'),
    ],
    [
        InlineKeyboardButton('🆘 Ajutor & Comenzi 🆘', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🇷🇴România HUB", url='https://github.com/LushaiMusic/VCMusicPlayer'),
        ],
        [
            InlineKeyboardButton('👥 Without Borders', url='https://t.me/withoutbordershub'),
            InlineKeyboardButton('Channel 📢', url='https://t.me/iZaute/6'),
        ],
        [
            InlineKeyboardButton('↗️ Distribuie grupul ↗️ 🔰', url='https://t.me/share/url?url=t.me/romuzicaro'),
            InlineKeyboardButton('🔰 Contact 🔰', url='http://t.me/HubContactBot'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{U}"]) & filters.user(Config.ADMINS))
async def restart(client, message):
    await message.reply_text("🔄 Restarting...")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
    os.execl(sys.executable, sys.executable, *sys.argv)

