import asyncio
import speedtest
from pyrogram import filters
from Bikash.Bgt import get_command
from Bikash import app
from Bikash.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**▷ 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭...**")
        test.download()
        m = m.edit("**▷ 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐔𝐩𝐥𝐨𝐚𝐝 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ 𝐑𝐔𝐊 𝐉𝐀𝐀 𝐀𝐁...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 𝟓 𝐒𝐄𝐂 𝐑𝐔𝐊 𝐉𝐀 𝐕𝐀𝐑𝐍𝐀 𝐆𝐀𝐍𝐃 𝐌𝐀𝐑 𝐋𝐔𝐍𝐆𝐀...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""🥀 **𝐆𝐀𝐍𝐃 𝐌𝐄 𝐃𝐀𝐋 𝐋𝐄 𝐀𝐁 𝐈𝐒𝐊𝐎** 🥀
    
<u>**❥͜𝐂𝐥𝐢𝐞𝐧𝐭͡ :**</u>
**» __𝐈𝐬𝐩 :__** {result['client']['isp']}
**» __𝐂𝐨𝐮𝐧𝐭𝐫𝐲 :__** {result['client']['country']}
  
<u>**❥͜͡𝐒𝐞𝐫𝐯𝐞𝐫 :**</u>
**» __𝐍𝐚𝐦𝐞 :__** {result['server']['name']}
**» __𝐂𝐨𝐮𝐧𝐭𝐫𝐲 :__** {result['server']['country']}, {result['server']['cc']}
**» __𝐒𝐩𝐨𝐧𝐬𝐨𝐫 :__** {result['server']['sponsor']}
**» __𝐋𝐚𝐭𝐞𝐧𝐜𝐲 :__** {result['server']['latency']}  
**» __𝐏𝐢𝐧𝐠 :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
