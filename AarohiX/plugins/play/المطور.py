from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["اوامر", "الاوامر"])
)
async def mmmezat(client, message):
    await message.reply_text(
        f"""مرحبًا بك عزيزي {message.from_user.mention} في قسم مميزات سورس cr ميوزك\nهنا تكتب الاوامر """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- المطور .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- مسح .", callback_data="close"
                    ),
                ],
            ]
        ),
    )

@app.on_message(
    command(["المطور", "مطور السورس", "السورس"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/712531ecafbed454b8bff.jpg",
        caption="~ Source Dark .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور السورس .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- قناة السورس . ", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
