from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🔄 Tutup", callback_data="close")],
    ]


def playlist_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text='Daftar Putar Grup',
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🔄 Tutup", callback_data="close")],
    ]


def play_genre_playlist(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text='INDONESIAN',
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text='HIP-HOP',
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text='KPOP',
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text='LOFI',
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text='SAD', callback_data=f"play_playlist {user_id}|{type}|Sad"
            ),
            InlineKeyboardButton(
                text='DJ', callback_data=f"play_playlist {user_id}|{type}|Weeb"
            ),
        ],
        [
            InlineKeyboardButton(
                text='TRAP',
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text='POP',
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Kembali",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🔄 Tutup", callback_data="close"),
        ],
    ]


def add_genre_markup(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text='✚ DJ',
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text='✚ SAD',
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text='✚ KPOP',
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text='✚ LOFI',
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text='✚ INDONESIAN',
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text='✚ HIP-HOP',
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text='✚ TRAP',
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text='✚ POP',
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Kembali", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🔄 Tutup", callback_data="close"),
        ],
    ]


def check_genre_markup(type, videoid, user_id):
    return [
        [
            InlineKeyboardButton(
                text='DJ', callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text='SAD', callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text='KPOP', callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text='LOFI', callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text='INDONESIAN',
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text='HIP-HOP',
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text='TRAP', callback_data=f"check_playlist {type}|Punjabi"
            ),
            InlineKeyboardButton(
                text='POP', callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="🔄 Tutup", callback_data="close")],
    ]


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    return [
        [
            InlineKeyboardButton(
                text='Daftar Putar Grup',
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🔄 Tutup", callback_data="close")],
    ]


def paste_queue_markup(url):
    return [
        [
            InlineKeyboardButton(text="▶️", callback_data='resumecb'),
            InlineKeyboardButton(text="⏸️", callback_data='pausecb'),
            InlineKeyboardButton(text="⏭️", callback_data='skipcb'),
            InlineKeyboardButton(text="⏹️", callback_data='stopcb'),
        ],
        [
            InlineKeyboardButton(
                text="Checkout Antrian Daftar Putar", url=f"{url}"
            )
        ],
        [InlineKeyboardButton(text="🔄 Tutup", callback_data='close')],
    ]


def fetch_playlist(user_name, type, genre, user_id, url):
    return [
        [
            InlineKeyboardButton(
                text=f"Putar {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Daftar putar", url=f"{url}")],
        [InlineKeyboardButton(text="🔄 Tutup", callback_data='close')],
    ]


def delete_playlist_markuup(type, genre):
    return [
        [
            InlineKeyboardButton(
                text='Ya! hapus',
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="Tidak!", callback_data='close'),
        ]
    ]
