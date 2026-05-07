import http.server
import socketserver
import threading
import discord
import os
import asyncio

# --- RENDER ÜÇÜN OYAQ QALMA SİSTEMİ ---
def keep_alive():
    port = int(os.environ.get("PORT", 8080))
    handler = http.server.SimpleHTTPRequestHandler
    # Portu dinləyirik ki, Render botun işlədiyini bilsin
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Web server {port} portunda aktivdir.")
        httpd.serve_forever()

# Bot başlamazdan əvvəl veb serveri arxa planda açırıq
threading.Thread(target=keep_alive, daemon=True).start()

# --- DISCORD BOT KODU ---
TOKEN = os.getenv("DISCORD_TOKEN")
MESAJ = "Hello IF YOU SELLING ANYTING dm my main <@301406575652765698> (Send msg request)"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Giriş edildi: {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if isinstance(message.channel, discord.DMChannel):
            print(f"DM gəldi: {message.author}")
            try:
                await asyncio.sleep(2) 
                await message.channel.send(MESAJ)
                print("Cavab göndərildi.")
            except Exception as e:
                print(f"Xəta: {e}")

client = MyClient()

if __name__ == "__main__":
    if TOKEN:
        # discord.py-self kitabxanası ilə işə salırıq
        try:
            client.run(TOKEN)
        except Exception as e:
            print(f"Giriş xətası: {e}")
    else:
        print("XƏTA: DISCORD_TOKEN tapılmadı!")
        
