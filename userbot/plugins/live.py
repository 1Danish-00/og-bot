"""Check if userbot alive or not . """


import asyncio , time
from telethon import events
from userbot import StartTime , catdef
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, catdef , catversion
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from platform import python_version, uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
USERNAME = str(Config.LIVE_USERNAME) if Config.LIVE_USERNAME else "@Jisan7509"
CAT_IMG = Config.ALIVE_PIC

@borg.on(admin_cmd(outgoing=True, pattern="live$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if CAT_IMG:
         cat_caption  = f"__**༄ MY BOT IS RUNNING SUCCESFULLY ༄**__\n\n"
         cat_caption += f"**✧✧ Database :** `Functioning normally!`\n"   
         cat_caption += f"**✧✧ Telethon version :** `{version.__version__}\n`"
         cat_caption += f"**✧✧ Catuserbot Version :** `{catversion}`\n"
         cat_caption += f"**✧✧ Python Version :** `{python_version()}\n\n`"
         cat_caption += f"**ღ** __**Cat**__🐱 __**is always with you, my master ღ\n\n**__"
         cat_caption += f"**✧✧ My peru Master:** [{DEFAULTUSER}]({USERNAME})\n"
         cat_caption += f"**✧✧ Uptime :** `{uptime}\n`"
         cat_caption += f"**✧✧ Contact [Hatake Kakashi](@kakashi09bot) For notes**\n\n"
         cat_caption +=	f"           **ღ** __**[DEPLOY MY REPO]**__(https://github.com/Jisan09/catuserbot) **ღ**"
         await borg.send_file(alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id)
         await alive.delete()
    else:
        await alive.edit(f"__**༄ MY BOT IS RUNNING SUCCESFULLY ༄**__\n\n"
                         "**✧✧ Database :** `Functioning normally!`\n"   
                         f"**✧✧ Telethon version :** `{version.__version__}\n`"
                         f"**✧✧ Catuserbot Version :** `{catversion}`\n"
                         f"**✧✧ Python Version :** `{python_version()}\n\n`"
                         "**ღ** __**Cat**__🐱 __**is always with you, my master ღ\n\n**__"
                         f"**✧✧ My peru Master:** [{DEFAULTUSER}]({USERNAME})\n"
                         f"**✧✧ Uptime :** `{uptime}\n`"
                         f"**✧✧ Contact [Hatake Kakashi](@kakashi09bot) For notes**\n\n"
                         f"           **ღ** __**[DEPLOY MY REPO]**__(https://github.com/Jisan09/catuserbot) **ღ**"
                        )         


CMD_HELP.update({"live": "`.live` :\
      \nUSAGE: Type .live to see wether your bot is working or not. "
}) 