import os
import io
import requests
import shutil 
import random
import re
import glob
import time

from io import BytesIO
from requests import get
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.sync import events
from .. import OWNER_ID, tbot
from PIL import Image, ImageDraw, ImageFont



@tbot.on(events.NewMessage(pattern="^/blogo ?(.*)"))
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

  if not quew:
     await event.reply('Please Give Me A Text For The Logo.')
     return
 pesan = await event.reply('Logo In A Process. Please Wait...')
 try:
    text = event.pattern_match.group(1)
    ok = event.get_reply_message
    randc = await tbot.download_media(ok)
#    img = Image.open(io.BytesIO(randc))
    draw = ImageDraw.Draw(ok)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "black"
    shadowcolor = "blue"
    fnt = glob.glob("./Dasha/resources/*")
    randf = random.choice(fnt)
    font = ImageFont.truetype(randf, 120)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y = ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black")
    fname = "dasha.png"
    img.save(fname, "png")
    await telethn.send_file(event.chat_id, file=fname, caption = f"Logo Made By [Dasha](t.me/dasha_probot)")         
    await pesan.delete()
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await event.reply(f'Error {e}')

