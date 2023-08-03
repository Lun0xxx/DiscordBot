# DiscordBot
#
# Created by Lun0xxx on 01/08/2023
#

import discord
from discord.ext import commands

class RolesCog(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
    
    ################################
    ########## Commandes ###########
    ################################

    @commands.command()
    async def show_perms(self, ctx : commands.Context) -> discord.Embed:
        '''
            Fonction représentant une commande permettant d'afficher toutes les permissions possibles d'un rôle.
            Elle prend en paramètre le bot lui-même et le contexte.
            Cette fonction renvoie un embed sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée

        '''
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        perms_embed = discord.Embed(
            title = 'Permissions',
            description = '~ Advanced\n~ All\n~ All_channel\n~ Elevated\n~ General\n~ Membership\n~ None (default)\n~ Stage\n~ Stage_moderator\n~ Text\n~ Voice'
        )
        return await ctx.send(embed=perms_embed)
    
    @commands.command()
    async def show_roles(self, ctx : commands.Context) -> discord.Embed:
        '''
            Fonction représentant une commande permettant d'afficher les rôles du serveur.
            Elle prend en paramètre le bot lui-même et le contexte.
            Cette fonction renvoie un embed sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée

        '''
        no_role = 1
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        roles_embed = discord.Embed(
            title = 'Rôles du serveur'
        )

        roles = ctx.guild.roles
        for role in roles:
            roles_embed.add_field(
                name = f'Rôle n°{no_role}',
                value = role.name,
                inline = False
            )
            no_role = no_role + 1

        return await ctx.send(embed=roles_embed)

    @commands.command()
    async def createrole(self, ctx : commands.Context, name : str, permission : str) -> discord.Message:
        '''
            Fonction représentant une commande permettant de créer un rôle.
            Elle prend en paramètre le bot lui-même, le contexte, le nom du rôle et la permission a attribuer au rôle.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param name(str)             :: Représente le nom du rôle
            :: param permission(str)       :: Représente le nom de la permission a attribuer au rôle

        '''
        dict_perms = {
            'advanced' :        discord.Permissions.advanced(),
            'all' :             discord.Permissions.all(),
            'all_channel' :     discord.Permissions.all_channel(),
            'none' :            discord.Permissions.none(),
            'elevated' :        discord.Permissions.elevated(),
            'general' :         discord.Permissions.general(),
            'membership' :      discord.Permissions.membership(),
            'stage' :           discord.Permissions.stage(),
            'stage_moderator' : discord.Permissions.stage_moderator(),
            'text' :            discord.Permissions.text(),
            'voice' :           discord.Permissions.voice()
        }
        
        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouvez pas utiliser cette commande dans les conversations privées.')
        
        has_permissions = ctx.author.guild_permissions.manage_permissions and ctx.author.guild_permissions.manage_roles
        if not has_permissions:
            return await ctx.send('Vous n\'avez pas les permissions requises pour créer un rôle')
        
        valid_perm = permission.lower() in dict_perms
        if not valid_perm:
            return await ctx.send(f'La permission {permission} n\'existe pas. Veuillez vous référer aux permissions de la commande !show_perms.')

        perm = dict_perms[permission.lower()]

        await ctx.guild.create_role(name=name, permissions=perm)

        return await ctx.send(f'{ctx.author.mention} a créé le rôle {name} avec la permission {permission}.')
    
    @commands.command()
    async def deleterole(self, ctx : commands.Context, name_role : str, *, reason : str = 'Aucune raison définie') -> discord.Message:
        '''
            Fonction représentant une commande permettant de supprimer un rôle.
            Elle prend en paramètre le bot lui-même, le contexte, le nom du rôle, et la raison (facultative) (par défaut : 'Aucune raison définie')
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param name_role(str)        :: Représente le nom du rôle
            :: param reason(str)           :: Représente la raison de la suppression du rôle

        '''
        role = None

        is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_messages:
            return await ctx.send('Vous ne pouveez pas utiliser cette commande dans les conversations privées.')
        
        has_permissions = ctx.author.guild_permissions.manage_roles
        if not has_permissions:
            return await ctx.send('Vous n\'avez pas les permissions requises pour supprimer ce rôle.')
        
        for roles in ctx.guild.roles:
            if name_role == roles.name:
                role = roles

        role_exists = not role is None
        if not role_exists:
            return await ctx.send(f'Le rôle {name_role} n\'existe pas.')
        
        await discord.Role.delete(role, reason=reason)

        return await ctx.send(f'{ctx.author.mention} a supprimé le rôle {role.name}.')
    
    ############################################
    ########### Gestion des erreurs ############
    ############################################
        
    @createrole.error
    async def createrole_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction représentant la gestion des erreurs de la commande !createrole.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur en question

        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un ou plusieurs argument(s). Exemple : !createrole <nom_du_role> <permission>')
        
    @deleterole.error
    async def deleterole_error(self, ctx : commands.Context, error) -> discord.Message:
        '''
            Fonction représentant la gestion des erreurs de la commande !deleterole.
            Elle prend en paramètre le bot lui-même, le contexte et l'erreur en question.
            Cette fonction renvoie un message sur le serveur Discord.

            :: param self()                :: Représente le bot
            :: param ctx(commands.Context) :: Représente le contexte (le channel) où la commande a été effectuée
            :: param error()               :: Représente l'erreur en question
            
        '''
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Il manque un ou plusieurs argument(s). Exemple : !deleterole <nom_du_role> <raison>')


async def setup(bot : commands.Bot) -> None:
    '''
        Fonction représentant une méthode main.
        Elle permet d'ajouter le cog au bot et de pouvoir être chargée lors de l'initialisation du bot.
        Elle prend en paramètre le bot.

        :: param bot(commands.Bot) :: Représente le bot
        
    '''
    await bot.add_cog(RolesCog(bot))