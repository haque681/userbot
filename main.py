from telethon import TelegramClient, events
import os

API_ID = int(os.environ.get("37868240"))
API_HASH = os.environ.get("01acf327ead2e1c9bcfa1aa6b8382453")
PHONE = os.environ.get("+8801733604025")

AUTO_REPLY = """
🔔 আমি এখন অফলাইন আছি।

আপনার মেসেজ পেয়েছি ✅
অনলাইনে ফিরলে রিপ্লাই করবো।

📝 জরুরি হলে বিস্তারিত লিখুন।
"""

client = TelegramClient("my_session", API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handler(event):
    await event.reply(AUTO_REPLY)

client.start(phone=PHONE)
client.run_until_disconnected()
