from pyrogram import Client, filters
from pyrogram.types import Message

from Yukki import SUDOERS, app
from Yukki.Database import blacklist_chat, blacklisted_chats, whitelist_chat

__MODULE__ = "Blacklist"
__HELP__ = """


/blacklistedchat 
- Periksa Obrolan Daftar Hitam Bot.


**Catatan:**
Hanya untuk Pengguna Sudo.


/blacklistchat [CHAT_ID] 
- Daftar hitam obrolan apa pun dari menggunakan Bot Musik


/whitelistchat [CHAT_ID] 
- Daftar putih obrolan apa pun yang masuk daftar hitam dari menggunakan Bot Musik

"""


@app.on_message(filters.command("blacklistchat") & filters.user(SUDOERS))
async def blacklist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**Penggunaan:**\n/blacklistchat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats():
        return await message.reply_text("Chat is already blacklisted.")
    blacklisted = await blacklist_chat(chat_id)
    if blacklisted:
        return await message.reply_text(
            "Obrolan telah berhasil masuk daftar hitam"
        )
    await message.reply_text("Terjadi kesalahan, periksa log.")


@app.on_message(filters.command("whitelistchat") & filters.user(SUDOERS))
async def whitelist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**Penggunaan:**\n/whitelistchat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats():
        return await message.reply_text("Obrolan sudah masuk daftar putih.")
    whitelisted = await whitelist_chat(chat_id)
    if whitelisted:
        return await message.reply_text(
            "Obrolan telah berhasil masuk daftar putih"
        )
    await message.reply_text("Terjadi kesalahan, periksa log.")


@app.on_message(filters.command("blacklistedchat"))
async def blacklisted_chats_func(_, message: Message):
    text = "**Obrolan Daftar Hitam:**\n\n"
    j = 0
    for count, chat_id in enumerate(await blacklisted_chats(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except Exception:
            title = "Private"
        j = 1
        text += f"**{count}. {title}** [`{chat_id}`]\n"
    if j == 0:
        await message.reply_text("Tidak Ada Obrolan Daftar Hitam")
    else:
        await message.reply_text(text)
