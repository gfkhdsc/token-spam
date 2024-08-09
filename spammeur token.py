import discord
import asyncio

# Afficher "TOKEN SPAM" en gros
print("########## TOKEN SPAM ##########")
print("#                               #")
print("#          TOKEN SPAM           #")
print("#                               #")
print("#################################\n")

class SelfBot(discord.Client):
    def __init__(self, message, cooldown, *args, **kwargs):
        # Définir les intents
        intents = discord.Intents.all()
        intents.guilds = True
        intents.messages = True
        # Appeler le constructeur parent avec les intents
        super().__init__(intents=intents, *args, **kwargs)
        self.message = message
        self.cooldown = cooldown

    async def on_ready(self):
        # Vérification du type de compte (utilisateur ou bot)
        if self.user.bot:
            print("Le token fourni est un token de bot. Veuillez fournir un token d'utilisateur.")
            await self.close()
            return

        print(f'Connecté en tant que {self.user}')
        while True:
            for guild in self.guilds:
                for channel in guild.text_channels:
                    try:
                        await channel.send(self.message)
                        print(f'Message envoyé à {channel.name} dans {guild.name}')
                    except Exception as e:
                        print(f'Impossible d\'envoyer un message à {channel.name} dans {guild.name} : {e}')
                    await asyncio.sleep(self.cooldown)
            # Optionnel : ajouter un délai entre les itérations complètes pour éviter le spam
            await asyncio.sleep(60)

def main():
    token = input("Entrez votre token Discord : ")
    message = input("Entrez le message à envoyer : ")
    cooldown = float(input("Entrez le délai entre les messages (en secondes) : "))
    
    bot = SelfBot(message=message, cooldown=cooldown)
    try:
        bot.run(token, bot=False)
    except discord.errors.LoginFailure:
        print("Le token fourni est invalide. Veuillez vérifier et réessayer.")

if __name__ == "__main__":
    main()

