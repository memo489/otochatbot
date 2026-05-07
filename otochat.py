import discord
import os
import asyncio

# GitHub Secrets-dən tokeni götürürük
TOKEN = os.getenv("DISCORD_TOKEN")
MESAJ = "Hello IF YOU SELLING ANYTING dm my main <@301406575652765698> (Send msg request)"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Giriş edildi: {self.user}')

    async def on_message(self, message):
        # Öz mesajımıza cavab vermirik
        if message.author == self.user:
            return

        # Yalnız DM gəldikdə cavab ver
        if isinstance(message.channel, discord.DMChannel):
            print(f"DM gəldi: {message.author}")
            try:
                await asyncio.sleep(2) # 2 saniyə gözlə ki, bot olduğu çox bəlli olmasın
                await message.channel.send(MESAJ)
                print("Cavab göndərildi.")
            except Exception as e:
                print(f"Xəta: {e}")

client = MyClient()

if __name__ == "__main__":
    if TOKEN:
        # 'bot=False' hissəsini sildik, çünki discord.py-self bunu avtomatik bilir
        client.run(TOKEN) 
    else:
        print("TOKEN TAPILMADI!")
        
        
