"""Checker.py."""

from typing import Union, Optional, TypedDict

import requests
import discord

Channel = Union[
    discord.abc.GuildChannel,
    discord.Thread,
    discord.abc.PrivateChannel
]


class APIResponse(TypedDict):
    """Alamo API."""
    unique_id: str
    presentation_slug: str
    show_time_local: str
    status: str
    ticket_count: str


class MPTChecker(object):
    """MPTchecker class."""
    def __init__(self, channel: Optional[Channel]) -> None:
        """Checker init."""
        self.shows: dict[str, APIResponse] = dict()
        self.channel = channel

    async def check(self) -> None:
        """Check method."""
        if self.channel is None:
            return

        if hasattr(self.channel, "send"):
            await self.channel.send("checking")
        url = (
            'https://drafthouse.com/s/mother'
            '/v2/schedule/collection/austin/master-pancake'
        )

        r = requests.get(url)
        # main per-request block

        data = r.json()
        for session in data["data"]["sessions"]:
            presentation_slug = session["presentationSlug"]
            show_time_local = session["showTimeClt"]
            status = session["status"]
            ticket_count = session["ticketTypesVoucherCount"]

            unique_id = f"{presentation_slug}@{show_time_local}"
            cinema_id = session["cinemaId"]
            session_id = session["sessionId"]
            link_url = (
                "https://drafthouse.com/austin/show/"
                f"{presentation_slug}?cinemaId={cinema_id}"
                f"&sessionId={session_id}&showSeats=true"
            )

            if unique_id not in self.shows:
                self.shows[unique_id] = {
                    "unique_id": unique_id,
                    "presentation_slug": presentation_slug,
                    "show_time_local": show_time_local,
                    "status": status,
                    "ticket_count": ticket_count
                }

                if hasattr(self.channel, "send"):
                    await self.channel.send((
                        f"New show listed: {unique_id} "
                        f"with status {status}: {link_url}"
                    ))

            show = self.shows[unique_id]

            if status != show["status"]:
                if hasattr(self.channel, "send"):
                    await self.channel.send((
                        f"Show status: {unique_id} "
                        f"changed from {show['status']} to {status}: {link_url}"
                    ))
