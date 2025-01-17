# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

"""for stuff related to android"""

from bs4 import BeautifulSoup
from requests import get

from userge import Message, userge


@userge.on_cmd(
    "twrp",
    about={"header": "Find twrp for you device", "usage": "{tr}twrp <device codename>"},
    allow_via_bot=True,
)
async def device_recovery(message: Message):
    """Get Latest TWRP"""
    message.reply_to_message
    args = message.filtered_input_str
    if args:
        device = args
    else:
        await message.err("```Provide Device Codename !!```", del_in=3)
        return
    await message.delete()
    url = get(f"https://dl.twrp.me/{device}/")
    if url.status_code == 404:
        reply = f"`Couldn't find twrp downloads for {device}!`\n"
        return await message.edit(reply, del_in=5)
    page = BeautifulSoup(url.content, "lxml")
    download = page.find("table").find("tr").find("a")
    dl_link = f"https://dl.twrp.me{download['href']}"
    dl_file = download.text
    size = page.find("span", {"class": "filesize"}).text
    date = page.find("em").text.strip()
    reply = (
        f"**Latest TWRP for {device}:**\n"
        f"[{dl_file}]({dl_link}) - __{size}__\n"
        f"**Updated:** __{date}__"
    )
    await message.edit(reply)


@userge.on_cmd("magisk$", about={"header": "Get Latest Magisk Zip and Manager"})
async def magisk_(message: Message):
    """Get Latest MAGISK"""
    magisk_repo = "https://raw.githubusercontent.com/topjohnwu/magisk-files/"
    magisk_dict = {
        "⦁ 𝗦𝘁𝗮𝗯𝗹𝗲": magisk_repo + "master/stable.json",
        "⦁ 𝗕𝗲𝘁𝗮": magisk_repo + "master/beta.json",
        "⦁ 𝗖𝗮𝗻𝗮𝗿𝘆": magisk_repo + "master/canary.json",
    }
    releases = "<code><i>𝗟𝗮𝘁𝗲𝘀𝘁 𝗠𝗮𝗴𝗶𝘀𝗸 𝗥𝗲𝗹𝗲𝗮𝘀𝗲:</i></code>\n\n"
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += (
            f'{name}  :   [APK v{data["magisk"]["version"]}]({data["magisk"]["link"]})\n'
        )

    await message.edit(releases, disable_web_page_preview=True)

@userge.on_cmd("delta", about={"header": "Get Latest Delta Zip and Manager"})
async def magisk_(message: Message):
    """Get Latest DELTA"""
    delta_repo = "https://raw.githubusercontent.com/HuskyDG/magisk-files/main/"
    delta_dict = {
        "⦁ Debug": delta_repo + "debug.json",
        "⦁ Canary": delta_repo + "canary.json", 
    }
    releases = "<code>𝗟𝗮𝘁𝗲𝘀𝘁 Delta 𝗥𝗲𝗹𝗲𝗮𝘀𝗲:</code>\n\n"
    for name, release_url in delta_dict.items():
        data = get(release_url).json()
        releases += (
            f'{name}  :   [APK v{data["magisk"]["version"]}]({data["magisk"]["link"]})\n'
        )

    await message.edit(releases, disable_web_page_preview=True)