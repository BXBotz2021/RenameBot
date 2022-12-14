import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert ,find_one
from pyrogram.file_id import FileId
CHANNEL = os.environ.get("CHANNEL", "")
import datetime

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Good morning."
elif 12 <= currentTime.hour < 18:
	wish = 'Good afternoon.'
else:
	wish = 'Good evening.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	👋 нєℓℓσ {message.from_user.first_name }

	Iᴀᴍ Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ, Sᴇɴᴛ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Dᴏᴄᴜᴍᴇɴᴛ Oʀ Vɪᴅᴇᴏ Aɴᴅ Eɴᴛᴇʀ Nᴇᴡ Fɪʟᴇɴᴀᴍᴇ To Rᴇɴᴀᴍᴇ Iᴛ__😌""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("🔰 Cʜᴀɴɴᴇʟ" ,url="https://t.me/Movies_Botz") ], 
	[InlineKeyboardButton("🤖 Cʀᴇᴀᴛᴏʀ", url="https://t.me/MufazTG") ]  ]))



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("__Yᴏᴜ Aʀᴇ Nᴏᴛ Sᴜʙsᴄʀɪʙᴇᴅ Mʏ Cʜᴀɴɴᴇʟ__👀 ",reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("Subscribe ↗️" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       date = message.date
       _used_date = find_one(user_id)
       used_date = _used_date["date"]      
       c_time = time.time()
       LIMIT = 30
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:
       	await app.send_chat_action(message.chat.id, "typing")
       	await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```",reply_to_message_id = message.message_id)
       else:
       	
       	media = await client.get_messages(message.chat.id,message.message_id)
       	file = media.document or media.video or media.audio 
       	dcid = FileId.decode(file.file_id).dc_id
       	filename = file.file_name
       	filesize = humanize.naturalsize(file.file_size)
       	fileid = file.file_id
       	await message.reply_text(f"""__ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ🧐?__\n\n**Fɪʟᴇ Nᴀᴍᴇ** :- {filename}\n**Fɪʟᴇ Siᴢᴇ** :- {filesize}\n**DC ID** :- {dcid} """,reply_to_message_id = message.message_id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ",callback_data = "rename"),InlineKeyboardButton("⛔ Cᴀɴᴄᴇʟ ",callback_data = "cancel")  ]]))
