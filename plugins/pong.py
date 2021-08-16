# originally writen by @levina-lab on github
# copyright (C) 2021 by veez project

"""
📚 Commands Available -
• `{i}pong`
   ketik <handler>pong untuk melihat kecepatan 𝙞𝙘𝙡𝙭𝙪𝙨𝙚𝙧𝙗𝙤𝙩 mu.
"""

import asyncio

@ultroid_cmd(pattern="pong")
async def dsb(ult):
	await ult.edit("`pong!....`")
	await asyncio.sleep(0.5)
	await ult.edit("`pong..!..`")
	await asyncio.sleep(0.5)
	await ult.edit("`pong....!`")
	await asyncio.sleep(0.5)
	await ult.edit("`✨✨ PING ✨✨\n• 🚀 Kecepatan: 69.69ms\n• 🤖 𝙞𝙘𝙡𝙭𝙪𝙨𝙚𝙧𝙗𝙤𝙩 by:`@icalasli")
	
# By @levina-lab 😁

