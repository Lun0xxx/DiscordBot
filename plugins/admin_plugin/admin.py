# DiscordBot
#
# Created by Lun0xxx on 01/08/2023
#

import discord
from discord.ext import commands
import random

class AdminCog(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    ################################
    ########## Commandes ###########
    ################################

    @commands.command()
    async def kick(self, ctx : commands.Context, member : discord.Member, *, reason : str = "Aucune raison définie") -> discord.Message:
        ''' 
            Fonction représentant une commande de kick (exclusion).
            Elle prend en paramètre le bot lui-même, le contexte, un membre et une raison facultative (par défaut : 'Aucune raison définie').
            Cette fonction renvoie un message dans le serveur Discord.

            :: param self()                 :: Représente le bot
            :: param ctx(commands.Context)  :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre du serveur a exclure
            :: param reason(str)            :: Représente la raison de l'exclusion du membre

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        author_has_permissions = ctx.author.guild_permissions.kick_members
        if not author_has_permissions:
            return await ctx.send('Vous n\'avez pas les permissions requises pour kick ce membre.')
        
        author_can_kick = ctx.author.top_role > member.top_role
        if not author_can_kick:
            return await ctx.send('Vous ne pouvez pas kick ce membre car vos rôles sont inférieurs aux siens.'.format(member.name))
        
        await member.kick(reason=reason)

        return await ctx.send('Le membre {} a été kick par {} pour {}'.format(member.mention, ctx.author.mention, reason))
    
    @commands.command()
    async def ban(self, ctx : commands.Context, member : discord.Member, *, reason='Aucune raison définie') -> discord.Message:
        '''
            Fonction représentant une commande de ban (bannissement).
            Elle prend en paramètre le bot lui-même, le contexte, le membre et la raison (par défaut : 'Aucune raison définie')
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                 :: Représente le bot
            :: ctx(commands.Context)        :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre du serveur a bannir
            :: param reason(str)            :: Représente la raison du bannissement du membre

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        author_has_permissions = ctx.author.guild_permissions.ban_members
        if not author_has_permissions:
            return await ctx.send('Vous n\'avez pas les permissions requises pour bannir ce membre.')
        
        author_can_ban = ctx.author.top_role > member.top_role
        if not author_can_ban:
            return await ctx.send('Vous ne pouvez pas bannir ce membre car vos rôles sont inférieurs aux siens.')
        
        await member.ban(reason=reason)

        return await ctx.send('Le membre {} a été banni par {} pour {}.'.format(member.mention, ctx.author.mention, reason))
    
    @commands.command()
    async def unban(self, ctx : commands.Context, member : str) -> discord.Message:
        '''
            Fonction représentant une commande d'unban (débannissement).
            Elle prend en paramètre le bot lui-même, le contexte et le membre a débannir.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                 :: Représente le bot
            :: param ctx(commands.Context)  :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre a débannir

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans une conversation privée.')
        
        author_has_permissions = ctx.author.guild_permissions.ban_members
        if not author_has_permissions:
            return await ctx.send('Vous n\'avez pas les permissiosn requises pour débannir ce membre.')
        
        roles = sorted(ctx.guild.roles)
        author_can_unban = roles[-1] in ctx.author.roles
        if not author_can_unban:
            return await ctx.send(f'Vous n\'avez pas les permissions requises pour débannir ce membre.\n'
                                  f'Seulement les personnes avec le rôle {roles[-1]} peuvent débannir ce membre.\n'
                                  f'Si vous le possédez, vérifiez que le rôle {roles[-1]} soit placé en tête de liste dans la liste des rôles.')
        
        banned_users = [user async for user in ctx.guild.bans()]
        member_name, member_discriminator = member.split('#')

        for user_banned in banned_users:
            user = user_banned.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return await ctx.send('Le membre {} a été débanni par {}.'.format(ctx.author.mention, user.mention))

        return await ctx.send('Le membre {} ne se trouve pas parmi les bannis.'.format(member))
    
    @commands.command()
    async def clear(self, ctx : commands.Context, limit : int = 5) -> discord.Message:
        '''
            Fonction représentant une commande de clear (nettoyage).
            Cela permet de nettoyer un channel Discord d'un nombre de messages donné.
            Elle prend en paramètre le bot lui-même, le contexte et la limite (par défaut : 5).
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param limit(int)            :: Représente le nombre de messages a supprimer

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        author_has_permissions = ctx.author.guild_permissions.manage_messages
        if not author_has_permissions:
            return await ctx.send('Vous n\'avez pas les permissions requises pour clear le channel.')
        
        await ctx.channel.purge(limit=limit + 1)

        return await ctx.send(' {} a purgé le channel de {} messages.'.format(ctx.author.mention, limit))
    
    ############################################
    ########### Gestion des erreurs ############
    ############################################

    @kick.error
    async def kick_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction permettant de gérer les cas d'erreurs de la commande !kick.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message dans le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur retournée

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un ou plusieurs argument(s). Exemple : !kick <membre> <raison>')
        
    @ban.error
    async def ban_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction permettant de gérer les cas d'erreurs de la commande !ban.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message dans le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur retournée

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un ou plusieurs argument(s). Exemple : !ban <membre> <raison>')
        
    @unban.error
    async def unban_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction permettant de gérer les cas d'erreurs de la commande !unban.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message dans le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur retournée

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un argument. Exemple : !unban <membre>')
    
async def setup(bot : commands.Bot) -> None:
    '''
        Fonction représentant une méthode main.
        Elle permet d'ajouter le cog au bot et de pouvoir être chargée lors de l'initialisation du bot.
        Elle prend en paramètre le bot.

        :: param bot(commands.Bot) :: Représente le bot
        
    '''
    await bot.add_cog(AdminCog(bot))