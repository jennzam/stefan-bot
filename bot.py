import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {0}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content:
            with open("stefans_quotes.txt", "r", encoding="utf-8") as file:
                quotes = file.readlines()

            if quotes:
                import random
                quote = random.choice(quotes).strip()
                await message.channel.send(quote)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))

