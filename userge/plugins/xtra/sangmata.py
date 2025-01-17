""" Sangmata """

# By @Krishna_Singhal
# Fixed Bedircan AYAYDIN 

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from userge import Message, userge
from userge.utils.exceptions import StopConversation


@userge.on_cmd(
    "sg",
    about={
        "header": "Sangmata gives you user's last updated names and usernames.",
        "flags": {"-u": "To get Username history of a User"},
        "usage": "{tr}sg [Reply to user]\n" "{tr}sg -u [Reply to user]",
    },
)
async def sangmata_(message: Message):
    """Get User's Updated previous Names and Usernames"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get Name and Username History...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@SangMata_BOT"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @SangMata_BOT, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/search_id {}".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    name = "Name History"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(name):
                await message.edit(f"`{msg.text}`")
