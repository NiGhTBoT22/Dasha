from Dasha.events import dasha
from Dasha import ubot, tbot, xbot, abot
from telethon import events
import subprocess, asyncio, traceback, io, sys, os, time
import requests
import asyncio

@dasha(pattern="^/exec ?(.*)")
async def ebent(event):
    if event.fwd_from:
        return
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return await event.edit("What should i execute?..")
    catevent = await event.edit("`Executing.....`")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    curruser = "TAMILVIP007"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"`{curruser}:~#` `{cmd}`\n`{result}`"
    else:
        cresult = f"`{curruser}:~$` `{cmd}`\n`{result}`"
    await catevent.edit(cresult)
    
    
@dasha(pattern="^/eval ?(.*)")
@xbot.on(events.NewMessage(from_users=[2048431295, 2062977461],pattern="[.]eval  ?(.*)"))
@abot.on(events.NewMessage(from_users=[2079472115, 1656231403],pattern="[.]eval  ?(.*)"))
async def _(event):
    if len(event.text) > 5 and event.text[5] != " ":
        return
  #  xx = await event.edit('`Processing..`')
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await xx.edit('`Give some code`')
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    reply_to_id = event.message.id
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = ("Success")

    final_output = "**OUTPUT**:\n\n`{}`".format(evaluation)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    if len(final_output) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await ubot.send_file(
                event.chat_id,
                out_file,
                thumb="Dasha/resources/Dasha.jpg",
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )

    else:
        await event.reply(final_output)
        
async def aexec(code, event):
    exec(
        (
            (
                ("async def __aexec(e, client): " + "\n message = event = e")
                + "\n reply = await event.get_reply_message()"
            )
            + "\n chat = (await event.get_chat()).id"
        )
        + "".join(f"\n {l}" for l in code.split("\n"))
    )

    return await locals()["__aexec"](event, event.client)
