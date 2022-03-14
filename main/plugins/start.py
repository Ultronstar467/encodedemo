#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

from .. import Drone, ACCESS_CHANNEL, AUTH_USERS
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG0 as file
from LOCAL.localisation import JPG4
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK
from ethon.teleutils import mention
from ethon.mystarts import vc_menu
from main.plugins.actions import set_thumbnail, rem_thumbnail, heroku_restart

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'👋 Hey [{event.sender.first_name}](tg://user?id={event.sender_id}) ♡\n\nI am Telegram Most Powerful Video Convertor Bot\n\nUse Help Button to know How to use me\n\nMaintained By : @Tellybots', 
                      buttons=[[
                         Button.inline("🌌 Set Thumb", data="sett"),
                         Button.inline("🗑️ Del Thumb", data='remt')],
                         [
                         Button.inline("❔ Help", data="plugins"),
                         Button.inline("🗜️ Restart", data="restart")],
                         [
                         Button.inline("♨️ Close ", data="close")]])

    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} started the BOT')
    

    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)

@Drone.on(events.callbackquery.CallbackQuery(data="close"))
async def close(event):
    await event.delete()
    

    

