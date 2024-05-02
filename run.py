from application import create_app
import asyncio

async def main():
    dp, bot = create_app()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())