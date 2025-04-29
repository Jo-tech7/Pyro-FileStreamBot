import time
import logging
from pyrogram import idle
from WebStreamer import web, start
from WebStreamer.vars import Var
from WebStreamer.bot import StreamBot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Sleeping 10 seconds for time sync...")
    time.sleep(10)

    try:
        logger.info("Starting bot...")
        await start()
        logger.info("Bot started. Idling...")
        await idle()
        logger.info("Bot stopped.")

    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
