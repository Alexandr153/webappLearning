from core.config.config import bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands() -> None:
    commands = [
        BotCommand(
            command='start',
            description='Аннотация бота'
        ),
        BotCommand(
            command='menu',
            description='Основное меню бота'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
