# DiscordBot

🇫🇷 Français

Voici un bot Discord avec certaines fonctionnalités interessantes.

# Utilisation

Tout d'abord, il faut installer Python.
[Pour cela, rendez-vous sur ce site :] (https://www.python.org/downloads/) et téléchargez la version la plus récente et adaptée a votre système d'exploitation.

Ensuite, il faudra installer un autre outil, nommé Pip.
[Pour cela, rendez-vous sur le site : (Windows) :] (https://waytolearnx.com/2020/06/comment-installer-pip-pour-python-sur-windows.html)
                                     [(macOS / Linux) :] (https://stacklima.com/comment-installer-pip-dans-macos/)

De plus, vous devrez installer le module **'discord.py'** pour faire fonctionner le bot.
Pour cela, rendez-vous dans un cmd (pour Windows) ou un terminal (pour macOS / Linux) et tapez la commande : **pip install discord.py**

[Maintenant, allez sur le portail développeur de Discord :] (https://discord.com/developers/docs/intro)
Vous vous connectez.
Créez une application (avec le bouton New Application).
Entrez le nom de votre bot.
Cochez la case et appuyez sur Créer.
Vous pouvez maintenant ajouter une image à votre bot, modifier son nom etc.
Vous allez appuyer sur **'Bot'** dans le menu déroulant à gauche.
Ensuite, vous descendez jusqu'à la section **'Privileged Gateway Intents'** et vous cochez les 3 options.
Vous retournez sur le menu déroulant à gauche, vous appuyez sur **'OAuth2'** puis **'URL Generator'**.
Dans **'Scopes'**, vous cochez **'bot'** et **'applications.commands'**.
Ensuite, dans **'Bot Permissions'**, vous cochez **'Administrator'** et vous récupérez le lien pour inviter le bot dans votre serveur.
Une fois fait, vous repartez dans le menu déroulant à gauche et vous appuyez sur **'Bot'**.
Au niveau de **'TOKEN'**, à côté du logo de votre Bot, vous appuyez sur **'Reset Token'** et vous le copiez.
***AVERTISSEMENT : Le token n'est a donner à personne. En cas de divulgation, le bot peut être utilisé par n'importe qui possédant le token jusqu'à ce que vous faîtes un reset du token à cet endroit.***
Une fois le token copié, vous vous rendez dans le dossier où se trouve les fichiers téléchargés et vous ouvrez le fichier **'.env'**.
Vous copiez ensuite votre token entre les guillements **(exemple : BOT_TOKEN='votre_token')**
Une fois cela fait, vous pouvez démarrer le bot en ouvrant un CMD (pour Windows) ou un terminal (pour macOS / Linux).
Vous vous rendez dans le dossier du projet et marquer la commande **'python3 main.py'**.
(Exemple Windows : Si le fichier se trouve dans le disque local C, alors vous tapez dans le cmd : **dir 'C:'** et vous tapez **'python main.py'**)
(Exemple macOS / Linux : Si le fichier se trouve dans vos téléchargements, vous tapez dans le terminal : **cd '~/Téléchargements'** ou **cd '~/Downloads'** et vous tapez **'python3 main.py'**)
Une fois qu'il est marqué **'Bot is running...'** cela indique que votre bot est en ligne.

Liste des commandes : 
    
    *!kick*
    Permet de kick un membre
    (Il y a deux arguments : le membre, la raison (facultative))
    Exemples d'utilisation : !kick @abcd
                             !kick @abcd Insultes

    *!ban*
    Permet de ban un membre
    (Il y a deux arguments : le membre, la raison (facultative))
    Exemples d'utilisation : !ban @abcd
                             !ban @abcd Comportement irrespectueux

    *!unban*
    Permet de débannir un membre
    (Il y a un seul argument : le membre)
    Exemple d'utilisation : !unban abcd#0000

    !clear
    Permet de supprimer autant de messages dans un salon
    (Il y a un seul argument : la nombre de messages (par défaut : 5))
    Exemples d'utilisation : !clear (5 messages seront effacés)
                             !clear 20 (20 messages seront effacés)

    !roll
    Permet de simuler un lancer de dès et obtenir un chiffre entre 1 et 6
    (Il n'y a pas d'arguments)
    Exemple d'utilisation : !roll

    !flip
    Permet de jouer au pile ou face
    (Il n'y a pas d'arguments)
    Exemple d'utilisation : !flip

    !serverinfos
    Permet d'obtenir quelques infos sur le serveur
    (Il n'y a pas d'arguments)
    Exemple d'utilisation : !serverinfos

    !userinfo
    Permet d'obtenir quelques infos sur un membre
    (Il y a un seul argument : le membre)
    Exemple d'utilisation : !userinfo @abcd

    !show_avatar
    Permet d'afficher l'avatar d'un membre dans le salon
    (Il y a un seul argument : le membre)
    Exemple d'utilisation : !show_avatar @abcd

    !warn
    Permet de donner un avertissement a un membre
    (Il y a deux arguments : le membre et la raison (facultative))
    Exemples d'utilisation : !warn @abcd
                             !warn @abcd Violent

    !show_warns
    Permet d'afficher tous les avertissements donnés à un membre
    (Il y a un seul argument : le membre)
    Exemple d'utilisation : !show_warns @abcd

    !clearwarns
    Permet d'effacer tous les avertissements donnés à un membre
    (Il y a un seul argument : le membre)
    Exemple d'utilisation : !clearwarns @abcd

    !show_perms
    Permet d'afficher toutes les permissions possibles à attribuer a un rôle
    (Il n'y a pas d'arguments)
    Exemple d'utilisation : !show_perms

    !show_roles
    Permet d'afficher tous les rôles présents dans le serveur
    (Il n'y a pas d'arguments)
    Exemple d'utilisation : !show_roles

    !createrole
    Permet de créer un rôle dans le serveur
    (Il y a deux arguments : le nom du rôle, et la permission) 
    (ATTENTION : Veillez à donner une seule des permissions possible depuis la commande !show_perms, seule la première sera prise en compte)
    Exemple d'utilisation : !createrole admin advanced

    !deleterole
    Permet de supprimer un rôle du serveur
    (Il y a deux arguments : le nom du rôle, la raison (facultative))
    Exemples d'utilisation : !deleterole admin 
                             !deleterole admin Changement des rôles

                             
