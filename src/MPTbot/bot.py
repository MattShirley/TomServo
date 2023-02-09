"""bot.py."""

import asyncio
import discord
import os

from .checker import MPTChecker


CHANNEL_ID = os.getenv("CHANNEL_ID")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

print(CHANNEL_ID, DISCORD_TOKEN)


class MPTbot(discord.Client):
    """MPTbot class for interacting with Discord."""
    async def setup_hook(self) -> None:
        """Discord setup method."""
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.look_for_tickets())

    async def look_for_tickets(self) -> None:
        """Main entrypoint to MPTchecker."""
        await self.wait_until_ready()

        if CHANNEL_ID is None:
            raise TypeError()
        channel_id = int(CHANNEL_ID)

        channel = self.get_channel(channel_id)
        checker = MPTChecker(channel)

        while not self.is_closed():
            if checker is not None:
                await checker.check()
            await asyncio.sleep(10)


def start_bot() -> None:
    """Main bot.py function."""
    print("starting bot")
    client = MPTbot(intents=discord.Intents.default())
    if DISCORD_TOKEN is not None:
        client.run(DISCORD_TOKEN)
