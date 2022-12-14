
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("🔰 Bot :- Rename Bot\n🎭 Creater :- @MufazTG\n🌍 Language :-Python3\n💡 Library :- Pyrogram\n✅ Server :- VPS")
