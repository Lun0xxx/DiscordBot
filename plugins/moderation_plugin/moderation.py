# DiscordBot
#
# Created by Lun0xxx on 01/08/2023
#

import discord
from discord.ext import commands
from datetime import datetime

class ModerationCog(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        self.warns = {}

    ################################
    ########## Commandes ###########
    ################################

    @commands.command()
    async def warn(self, ctx : commands.Context, member : discord.Member, *, reason : str = 'Aucune raison définie') -> discord.Message:
        '''
            Fonction représentant une commande permettant de donner un avertissement à un membre.
            Elle prend en paramètre le bot lui-même, le contexte, le membre et la raison (facultative) (par défaut : 'Aucune raison définie').
            Cette fonction renvoie un mesage sur le serveur Discord.

            :: param self()                 :: Représente le bot 
            :: param ctx(commands.Context)  :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre a avertir
            :: param reason(str)            :: Représente la raison de l'avertissement

        '''
        warning_embed = discord.Embed(
            title = 'Avertissement',
            description = f'Vous avez reçu un avertissement pour {reason}.',
            color = discord.Color.red(),
            timestamp = datetime.now()
        )
        warning_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        author_has_permissions = ctx.author.guild_permissions.manage_channels
        if not author_has_permissions:
            return await ctx.send('Vous n\'avez pas les permissions requises pour donner un avertissement à ce membre.')
        
        member_is_warnable = ctx.author.top_role > member.top_role
        if not member_is_warnable:
            return await ctx.send('Vous ne pouvez pas donner d\'avertissements à ce membre car vos rôles sont inférieurs aux siens.')
        
        warning = {
            'reason' : reason,
            'date' : datetime.now()
        }

        if member.name in self.warns:
            self.warns[member.name].append(warning)
        else:
            self.warns[member.name] = [warning]
        
        return await ctx.send(member.mention, embed=warning_embed)
    
    @commands.command()
    async def show_warns(self, ctx : commands.Context, member : discord.Member) -> discord.Embed:
        '''
            Fonction représentant une commande permettant d'afficher les avertissement d'un membre.
            Elle prend en paramètre le bot lui-même, le contexte et le membre.
            Cette fonction renvoie un embed sur le serveur Discord.

            :: param self()                 :: Représente le bot
            :: param ctx(commands.Context)  :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre en question

        '''
        numero_warn = 1
        warnings = discord.Embed(
            title = f'Avertissements de {member.name}'
        )
        warnings.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        has_permissions = ctx.author.guild_permissions.manage_channels
        if not has_permissions:
            return await ctx.send('Vous n\'avez pas les permissions requises pour utiliser cette commande.')
        
        warns_exists = member.name in self.warns
        if not warns_exists:
            return await ctx.send('Ce membre n\'a aucun avertissement enregistré.')
        
        for warns in self.warns[member.name]:
            warnings.add_field(
                name = f'Avertissement n°{numero_warn}',
                value = 'Raison : {}\nDate : {}'.format(warns['reason'], warns['date'].strftime('%d-%m-%Y'))
            )
            numero_warn = numero_warn + 1

        return await ctx.send(embed=warnings)
    
    @commands.command()
    async def clearwarns(self, ctx : commands.Context, member : discord.Member) -> discord.Message:
        '''
            Fonction représentant une commande permettant de supprimer tous les avertissements d'un membre.
            Elle prend en paramètre le bot lui-même, le contexte et le membre.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                 :: Représente le bot
            :: param ctx(commands.Context)  :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre en question

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        has_permissions = ctx.author.guild_permissions.administrator
        if not has_permissions:
            return await ctx.send('Seul l\'administrateur peut effacer les avertissements d\'un membre.')
        
        member_has_warns = member.name in self.warns
        if not member_has_warns:
            return await ctx.send('Ce membre ne possède pas d\'avertissements.')
        
        del self.warns[member.name]

        return await ctx.send(f'Tous les avertissements du membre {member.mention} ont été effacés.')
    
    ############################################
    ########### Gestion des erreurs ############
    ############################################

    @warn.error
    async def warn_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction représentant la gestion des erreurs de la commande !warn.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur en question

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un ou plusieurs argument(s). Exemple : !warn <membre> <raison>')
        
    @show_warns.error
    async def show_warns_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction représentant la gestion des erreurs de la commande !show_warns.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur en question

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un argument. Exemple : !show_warns <membre>')
        
    @clearwarns.error
    async def clearwarns_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction représentant la gestion des erreurs de la commande !clearwarns.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur en question

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un argument. Exemple : !clearwarns <membre>')
    
async def setup(bot : commands.Bot) -> None:
    '''
        Fonction représentant une méthode main.
        Elle permet d'ajouter le cog au bot et de pouvoir être chargée lors de l'initialisation du bot.
        Elle prend en paramètre le bot.

        :: param bot(commands.Bot) :: Représente le bot
        
    '''
    await bot.add_cog(ModerationCog(bot))