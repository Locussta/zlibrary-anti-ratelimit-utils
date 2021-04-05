import asyncio
import converter

loop = asyncio.get_event_loop()

print(loop.run_until_complete(converter.download_from_2lib('https://2lib.org/book/1014710/232998')))