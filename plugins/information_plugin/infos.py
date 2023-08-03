# DiscordBot
#
# Created by Lun0xxx on 01/08/2023
#

import discord
from discord.ext import commands
import random

class InformationsCog(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    ################################
    ########## Commandes ###########
    ################################

    @commands.command()
    async def serverinfos(self, ctx : commands.Context) -> discord.Embed:
        '''
            Fonction représentant une commande permettant d'afficher les infos du serveur.
            Elle prend en paramètre le bot lui-même et le contexte.
            Cette fonction renvoie un embed sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée

        '''
        online_members = [member for member in ctx.guild.members if member.status == discord.Status.online]
        infos_embed = discord.Embed(
            title = 'Infos Serveur',
            description = f'Nom : {ctx.guild.name}\nNombre de membres : {ctx.guild.member_count}\nEn ligne : {len(online_members)}',
            color = discord.Color.blue()
        )
        return await ctx.send(embed=infos_embed)
    
    @commands.command()
    async def userinfo(self, ctx : commands.Context, member : discord.Member) -> discord.Embed:
        '''
            Fonction représentant une commande permettant d'afficher les infos d'un membre.
            Elle prend en paramètre le bot lui-même, le contexte et le membre en question.
            Cette fonction renvoie un embed sur le serveur Discord.

            :: param self()                 :: Représente le bot
            :: param ctx(commands.Context)  :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre en question

        '''
        user_embed = discord.Embed(
            title = f'Infos de {member.name}'
        )
        user_embed.add_field(
            name = 'Nom',
            value = member.mention,
            inline = False
        )
        
        if not member.nick is None:
            user_embed.add_field(
                name = 'Surnom',
                value = member.nick,
                inline = False
            )

        if not member.activity is None:
            user_embed.add_field(
                name = 'Activité en cours',
                value = member.activity.name,
                inline = False
            )
        
        user_embed.add_field(
            name = 'Membre depuis',
            value = member.joined_at.strftime('%d-%m-%Y')
        )

        return await ctx.send(embed=user_embed)
    
    @commands.command()
    async def show_avatar(self, ctx : commands.Context, member : discord.Member) -> discord.DefaultAvatar:
        '''
            Fonction représentant une commande permettant d'afficher l'avatar d'un membre.
            Elle prend en paramètre le bot lui-même, le contexte et le membre en question.
            Cette fonction renvoie un avatar Discord sur le serveur Discord.

            :: param self()                 :: Représente le bot
            :: param ctx(commands.Context)  :: Représente le contexte (le channel) où la commande a été effectuée
            :: param member(discord.Member) :: Représente le membre en question

        '''
        return await ctx.send(member.display_avatar)
    
    ############################################
    ########### Gestion des erreurs ############
    ############################################

    @userinfo.error
    async def userinfo_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction représentant la gestion des erreurs de la commande !userinfo.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur en question

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un argument. Exemple : !userinfo <member>')
        
    @show_avatar.error
    async def show_avatar_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction représentant la gestion des erreurs de la commande !show_avatar.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectué
            :: param error()               :: Représente l'erreur en question

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un argument. Exemple : !show_avatar <member>')

async def setup(bot : commands.Bot) -> None:
    '''
        Fonction représentant une méthode main.
        Elle permet d'ajouter le cog au bot et de pouvoir être chargée lors de l'initialisation du bot.
        Elle prend en paramètre le bot.

        :: param bot(commands.Bot) :: Représente le bot
        
    '''
    await bot.add_cog(InformationsCog(bot))