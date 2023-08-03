# DiscordBot
#
# Created by Lun0xxx on 01/08/2023
#

import discord
from discord.ext import commands
import random

class DivertissementCog(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    ################################
    ########## Commandes ###########
    ################################

    @commands.command()
    async def roll(self, ctx : commands.Context) -> discord.Message:
        '''
            Fonction représentant une commande permettant d'avoir un chiffre au hasard entre 1 et 6.
            Elle prend en paramètre le bot lui-même et le contexte.
            Cette fonction renvoie un message dans le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')

        random_number = random.randint(1, 6)
        return await ctx.send(f'{ctx.author.mention} : {random_number}')        
    
    @commands.command()
    async def flip(self, ctx : commands.Context) -> discord.Message:
        '''
            Fonction représentant une commande permettant de tirer au sort Pile ou Face.
            Elle prend en paramètre le bot lui-même et le contexte.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        pile_face = ['Pile', 'Face']

        choix = random.randint(0, 1)

        return await ctx.send(f'{ctx.author.mention} : {pile_face[choix]}')

async def setup(bot : commands.Bot) -> None:
    '''
        Fonction représentant une méthode main.
        Elle permet d'ajouter le cog au bot et de pouvoir être chargée lors de l'initialisation du bot.
        Elle prend en paramètre le bot.

        :: param bot(commands.Bot) :: Représente le bot
        
    '''
    await bot.add_cog(DivertissementCog(bot))