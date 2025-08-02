import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        try:
            with open("stefan_quotes.txt", "r", encoding="utf-8") as file:
                quotes = file.readlines()

            if quotes:
                quote = random.choice(quotes).strip()
                await message.channel.send(quote)
        except Exception as e:
            print(f"Uh oh: {e}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))
