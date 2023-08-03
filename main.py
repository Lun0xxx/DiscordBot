# DiscordBot
#
# Created by Lun0xxx on 01/08/2023
#

import discord
from discord.ext import commands
import dotenv, os

class Bot(commands.Bot):
    def __init__(self) -> None:
        '''
            Fonction permettant d'initialiser le bot et d'y définir le préfixe des commandes et les intents.
            Elle prend en paramètre self qui représente le bot.

            :: param self() :: Représente le bot

        '''
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        '''
            Fonction permettant de charger tous les plugins du bot et de synchroniser le bot.
            Elle prend en paramètre self qui représente le bot.

            :: param self() :: Représente le bot

        '''
        await self.load_extension('plugins.admin_plugin.admin')
        await self.load_extension('plugins.moderation_plugin.moderation')
        await self.load_extension('plugins.information_plugin.infos')
        await self.load_extension('plugins.roles_plugin.roles')
        await self.load_extension('plugins.divertissement_plugin.divertissement')
        await self.tree.sync()

    async def on_ready(self) -> None:
        '''
            Fonction permettant d'afficher un message dans la console lorsque le bot est en ligne
            Elle prend en paramètre self qui représente le bot.

            :: param self() :: Représente le bot

        '''
        print("Bot is running...")

def main() -> None:
    '''
        Fonction main permettant de charger la variable d'environnement correspondante au token du bot et de le démarrer.
    '''
    dotenv.load_dotenv()
    TOKEN = os.getenv('BOT_TOKEN')

    if TOKEN is None:
        raise ValueError('Votre TOKEN n\'est pas défini')
    
    bot = Bot()
    bot.run(TOKEN)

if __name__ == "__main__":
    main()