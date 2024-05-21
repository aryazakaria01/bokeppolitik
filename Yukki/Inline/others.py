from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    return [[
            InlineKeyboardButton(
                text="🔎 Mencari Lirik",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ], [
            InlineKeyboardButton(
                text="Daftar Putar Anda",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="Daftar Putar Grup",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ], [
            InlineKeyboardButton(
                text="⬇️ Unduh Audio/Video",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ], [InlineKeyboardButton(
                text="⬅️ Kembali",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ), InlineKeyboardButton(text="🔄 Tutup", callback_data='close')]]


def download_markup(videoid, user_id):
    return [[
            InlineKeyboardButton(
                text="⬇️ Unduh Audio",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⬇️ Unduh Video",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ], [InlineKeyboardButton(
                text="⬅️ Kembali", callback_data=f"goback {videoid}|{user_id}"
            ), InlineKeyboardButton(text="🔄 Tutup", callback_data='close')]]
