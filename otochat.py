import http.server
import socketserver
import threading
import discord
import os
import asyncio

# --- RENDER ÜÇÜN OYAQ QALMA SİSTEMİ ---
def keep_alive():
    # Render avtomatik olaraq PORT təyin edir, yoxdursa 8080 istifadə edirik
    port = int(os.environ.get("PORT", 8080))
    handler = http.server.SimpleHTTPRequestHandler
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Web server {port} portunda aktivdir.")
            httpd.serve_forever()
    except Exception as e:
        print(f"Veb server xətası: {e}")

# Bot başlamazdan əvvəl veb serveri arxa planda açırıq
threading.Thread(target=keep_alive, daemon=True).start()

# --- DISCORD BOT KODU ---
TOKEN = os.getenv("DISCORD_TOKEN")
MESAJ = "Hello IF YOU SELLING ANYTING dm my main <@301406575652765698> (Send msg request)"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Sistem aktivdir! Giriş edilən hesab: {self.user}')

    async def on_message(self, message):
        # 1. Öz mesajlarımıza cavab vermirik (Döngünü sındırır)
        if message.author.id == self.user.id:
            return

        # 2. Yalnız Şəxsi Mesaj (DM) gəldikdə cavab veririk
        if isinstance(message.channel, discord.DMChannel):
            # Eyni adama təkrar-təkrar yazmasın deyə kiçik bir yoxlama
            print(f"DM mesajı gəldi: {message.author} (ID: {message.author.id})")
            
            try:
                # 3 saniyə gözləyirik (daha təbii görünməsi üçün)
                await asyncio.sleep(3) 
                await message.channel.send(MESAJ)
                print(f"Uğurla cavab verildi: {message.author}")
            except Exception as e:
                print(f"Mesaj göndərilərkən xəta baş verdi: {e}")

client = MyClient()

if __name__ == "__main__":
    if TOKEN:
        try:
            # discord.py-self üçün ən stabil giriş üsulu
            client.run(TOKEN)
        except Exception as e:
            print(f"Giriş zamanı ciddi xəta: {e}")
    else:
        print("XƏTA: DISCORD_TOKEN tapılmadı! Render Settings -> Environment Variables bölməsini yoxlayın.")
            
