
# import requests

# import discord
# import asyncio
# import datetime


# """
# cinemaId: 0004
# sessionId: 187344
# presentationSlug: choose-your-own-pancake
# legacySlug: choose-your-own-pancake
# status: SOLDOUT
# businessDateClt: 2023-02-10
# showTimeClt: 2023-02-10T22:00:00
# cinemaTimeZoneName: America/Chicago
# showTimeUtc: 2023-02-11T04:00:00
# ticketTypesLoyaltyCount: 0
# ticketTypesVoucherCount: 0
# ticketTypesNormalCount: 1
# reservedSeating: True
# screenNumber: 4
# formatSlug: 2d-digital
# isClosedCaptioningAvailable: False
# isDescriptiveAudioAvailable: False
# isAssistedListeningAvailable: False
# sessionAttributeSlugs: []
# recognitionIds: ['0']
# agePolicySlug: rated-r-0004
# isHidden: False
# ticketingExperience: DEFAULT
# """

# class MPTbot(discord.Client):
#     async def setup_hook(self) -> None:
#         # create the background task and run it in the background
#         self.bg_task = self.loop.create_task(self.look_for_tickets())

#     async def on_ready(self):
#         print(f'Logged in as {self.user} (ID: {self.user.id})')
#         print('------')

#     async def my_background_task(self):
#         await self.wait_until_ready()

#         counter = 0
#         channel = self.get_channel(1234567) # channel ID goes here

#         while not self.is_closed():
#             await channel.send(counter)
#             await asyncio.sleep(60)  # task runs every 60 seconds

#     async def look_for_tickets(self):
#         await self.wait_until_ready()
#         channel = self.get_channel(1234567)  # channel ID goes here

#         shows = dict()
#         while not self.is_closed():
            
#             url = 'https://drafthouse.com/s/mother/v2/schedule/collection/austin/master-pancake'

#             rs = requests.get(url)
#             print(rs)
#             # main per-request block
#             print("running")

#             data = r.json()
#             for session in data["data"]["sessions"]:
#                 presentation_slug = session["presentationSlug"]
#                 show_time_local = session["showTimeClt"]
#                 status = session["status"]
#                 ticket_count = session["ticketTypesVoucherCount"]

#                 unique_id = f"{presentation_slug}@{show_time_local}"
#                 cinema_id = session["cinemaId"]
#                 session_id = session["sessionId"]


#                 link_url = f"https://drafthouse.com/austin/show/{presentation_slug}?cinemaId={cinema_id}&sessionId={session_id}&showSeats=true"

#                 if unique_id not in shows:
#                     shows[unique_id] = {
#                         "unique_id": unique_id,
#                         "presentation_slug": presentation_slug,
#                         "show_time_local": show_time_local,
#                         "status": status,
#                         "ticket_count": ticket_count
#                     }
#                     channel.send(f"New show listed: {unique_id} with status {status}: {link_url}")
                
#                 show = shows[unique_id]

#                 if status != show["status"]:
#                     channel.send(f"Show status: {unique_id} changed from {show['status']} to {status}: {link_url}")
#             await asyncio.sleep(10)

# class MPTChecker(object):
#     pass



# client = MPTbot(intents=discord.Intents.default())
# client.run('token')
