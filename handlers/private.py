from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/68ba3f69f145217b02664.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ Sᴇxʏ ɢʀᴏᴜᴩ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ 🤗 Mʏ Lᴇᴀɢᴀɴᴅ Oᴡɴᴇʀ 👑 [∆I$H](https://t.me/aish_jaan_0) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Lᴇᴀɢᴀɴᴅ⚡", url="https://t.me/Xd_Lif")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ✨", url="https://t.me/LOVExWORD"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ🦋", url="https://t.me/LXW_UPDATE"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/camillamusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥Uᴩᴅᴀᴛᴇs", url="https://t.me/LXW_UPDATE")
                ]
            ]
        )
   )
