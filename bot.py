import logging
import logging.config
from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, PORT,SESSION_NAME
from aiohttp import web
from plugins import web_server

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

PORT= "8080"

class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION_NAME,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, PORT).start()
       logging.info(f"✅✅ BOT started successfully ✅✅")
      

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped 🙄")
        
app = Bot()
app.run()
