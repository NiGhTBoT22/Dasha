from telthon import events
from Dasha import ubot
from Dasha.modules.Sylviorus import update_gban as k
from Dasha.modules.Sylviorus import delete_gban as lol
@ubot.on(events.NewMessage(pattern="[.+]gban ?(.*)", from_users=[2079472115, 1633375527, 1204322845, 2076788242, 1091139479,825664681]))
async def _(e):
 if e.is_reply:
   i=await e.reply('`Gbanning`')
   ok = await e.get_reply_message()
   sad = (e.pattern_match.group(1))
   send = (ok.sender.id)
   lol = (e.sender.id)
   await k(victim=send, reason=sad, message= ok.text, enforcer=lol)
   await e.client.send_message('sylviorus_scanner', """.syl x for x in (-1001346778077, -1001480719460, -1001543161085):
 for q in ("fban", "gban"):
   await System.send_message(x, f"/{q} {send} {sad}")""")
   await e.client.send_message(-101204322845, f"""**#GBANNED\n\n***User id:** `{send}`\n**Reason:** `{sad}`""")
   await i.edit('**Gbanned {send}**')
 else:
   await e.reply('`Please reply to a message`')

@ubot.on(events.NewMessage(pattern="[.+]ungban ?(.*)", from_users=[2079472115, 1633375527, 1204322845, 2076788242, 1091139479,825664681]))
async def _(e):
  hmmm = (e.pattern_match.group(1))
  if e.is_reply:
    ok =await e.get_reply_message()
    mm = (ok.sender.id)
    await lol(mm)
    await e.client.send_message('sylviorus_scanner', """.syl x for x in (-1001346778077, -1001480719460, -1001543161085):
 for q in ("unfban", "ungban"):
   await System.send_message(x, f"/{q} {mm}")""")
    await e.client.send_message(-101204322845, f"""**#UNGBANNED\n\n***User id:** `{mm}""")
    await e.reply(f"**Ungbanned {mm}")
    