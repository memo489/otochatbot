import asyncio
import discord
import os

# --- RƏNGLƏR ---
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def ekrani_temizle():
    os.system("cls" if os.name == "nt" else "clear")

async def botu_baslat(token, mesaj):
    client = discord.Client(self_bot=True)

    @client.event
    async def on_ready():
        ekrani_temizle()
        print(f"{GREEN}===================================={RESET}")
        print(f"{GREEN} BOT İNDİ AKTİVDİR!{RESET}")
        print(f" Giriş edilən hesab: {client.user}")
        print(f"{GREEN}===================================={RESET}")
        print(f"{BLUE}Avtomatik Mesajınız:{RESET} {mesaj}")
        print(f"{YELLOW}Dayandırmaq üçün Ctrl + C basın.{RESET}\n")

    @client.event
    async def on_message(msg):
        # Öz mesajınsa heç nə etmə
        if msg.author == client.user:
            return

        # Yalnız DM-lərə cavab ver
        if msg.guild is None:
            print(f"{BLUE}[DM GƏLDİ]{RESET} Göndərən: {msg.author}")
            try:
                await asyncio.sleep(3)
                await msg.channel.send(mesaj)
                print(f"{GREEN}[CAVABLANDI]{RESET} Mesaj göndərildi.")
            except Exception as e:
                print(f"{RED}[XƏTA]{RESET} Göndərilmədi: {e}")

    try:
        await client.start(token)
    except Exception as e:
        print(f"{RED}[XƏTA]{RESET} Giriş alınmadı: {e}")

def main():
    # GitHub Actions-da işləməsi üçün tokeni 'Secrets'dən götürürük
    token = os.environ.get("DISCORD_TOKEN")
    mesaj = "Hello IF YOU SELLING ANYTING dm my main <@301406575652765698> (Send msg request)"
   
    if not token:
        print("Xəta: DISCORD_TOKEN tapılmadı!")
        return

    print(f"Bot başladılır...")
    
    try:
        asyncio.run(botu_baslat(token, mesaj))
    except Exception as e:
        print(f"Xəta: {e}")

if __name__ == "__main__":
    main()
      
