from core.utils.commands import set_commands
from core.config.config import dispatcher as dp

@dp.startup()
async def start_bot() -> None:
    await set_commands()
    print("[-] Бот начал работу")


@dp.shutdown()
async def stop_bot() -> None:
    print("[-] Бот закончил работу")