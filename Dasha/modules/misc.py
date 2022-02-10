from Dasha.events import dasha
import speedtest
import nekos
import requests
from telethon.sync import events
from Dasha import ubot
#Some misc modules

@dasha(pattern='^/stat')
async def stat(event):
      await event.edit(f'➤ 𝚃𝚘𝚝𝚊𝚕 𝙽𝚘 𝙾𝚏 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝙸𝚗 **{event.chat.title}** **:** `{event.id}`')
      
@dasha(pattern="^/vdl$")
async def lmao(event):
      x=await event.get_reply_message()
      sex=await event.edit('`Downloading...`')
      await event.client.download_media(x,f'{event.id}.mp4')
      await sex.edit('`Media Successfully dowmloaded.`')

@dasha(pattern="^/nekos ?(.*)")
async def nekos_img(event):
    arguments = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "goose",
    "baka",
    "woof",
    "kemonomimi",
    "smug",
    ]
    args = event.pattern_match.group(1)
    anos = await event.edit("`Fetching from nekos...`")
    pic = nekos.img(args)
    await ubot.send_file(event.chat_id,pic)
    await anos.delete()     
 
 
      
@dasha(pattern="^/meme")
async def lol(event):
    r = requests.get('https://nksamamemeapi.pythonanywhere.com').json()
    pic = r['image']
    title = r['title']
    await event.delete()
    await event.client.send_file(event.chat_id, pic , caption=title)

      
@dasha(pattern="^/hmeme")
async def lol(event):
    r = requests.get('https://nksamamemeapi.pythonanywhere.com/get/hentaimemes').json()
    pic = r['image']
    title = r['title']
    await event.delete()
    await event.client.send_file(event.chat_id, pic , caption=title)
    
