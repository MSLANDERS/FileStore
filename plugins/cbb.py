from pyrogram import Client 
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("☸️ Bᴀᴄᴋᴜᴘ", url="https://t.me/mslanders"),
                    InlineKeyboardButton("🎞 Mᴏᴠɪᴇ Gʀᴏᴜᴘ", url="https://t.me/msrequest_group")
                ],[
                    InlineKeyboardButton("👨‍💻 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/mslanders_help"),
                    InlineKeyboardButton("☎ Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ", url="https://t.me/mslanderstalk_bot")
                ],[
                    InlineKeyboardButton('Hᴏᴍᴇ 🪔', callback_data='start'),
                    InlineKeyboardButton("Cʟᴏꜱᴇ ⛔", callback_data='close')
                ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('Hᴏᴍᴇ 🪔', callback_data='start'),
                     InlineKeyboardButton('Cʟᴏꜱᴇ ⛔', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("✭ Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ ✭", url="https://t.me/mslanders")
                ],[
                    InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ 🍁", callback_data='help'),
                    InlineKeyboardButton("Aʙᴏᴜᴛ 💌", callback_data='about')
                ]]
            )
        )
    
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
