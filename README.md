# DiscordBot

🇫🇷 Français

Voici un bot Discord avec certaines fonctionnalités interessantes.

# Utilisation

1. Tout d'abord, il faut installer Python.
[Pour cela, rendez-vous sur ce site :] (https://www.python.org/downloads/) et téléchargez la version la plus récente et adaptée a votre système d'exploitation.

2. Ensuite, il faudra installer un autre outil, nommé Pip.
[Pour cela, rendez-vous sur le site : (Windows) :] (https://waytolearnx.com/2020/06/comment-installer-pip-pour-python-sur-windows.html)
                                     [(macOS / Linux) :] (https://stacklima.com/comment-installer-pip-dans-macos/)

De plus, vous devrez installer le module **'discord.py'** pour faire fonctionner le bot.
3. Pour cela, rendez-vous dans un cmd (pour Windows) ou un terminal (pour macOS / Linux) et tapez la commande : **pip install discord.py**

4. [Maintenant, allez sur le portail développeur de Discord :] (https://discord.com/developers/docs/intro)
5. Vous vous connectez.
6. Créez une application (avec le bouton New Application).
7. Entrez le nom de votre bot.
8. Cochez la case et appuyez sur Créer.
9. Vous pouvez maintenant ajouter une image à votre bot, modifier son nom etc.
10. Vous allez appuyer sur **'Bot'** dans le menu déroulant à gauche.
11. Ensuite, vous descendez jusqu'à la section **'Privileged Gateway Intents'** et vous cochez les 3 options.
12. Vous retournez sur le menu déroulant à gauche, vous appuyez sur **'OAuth2'** puis **'URL Generator'**.
13. Dans **'Scopes'**, vous cochez **'bot'** et **'applications.commands'**.
14. Ensuite, dans **'Bot Permissions'**, vous cochez **'Administrator'** et vous récupérez le lien pour inviter le bot dans votre serveur.
15. Une fois fait, vous repartez dans le menu déroulant à gauche et vous appuyez sur **'Bot'**.
16. Au niveau de **'TOKEN'**, à côté du logo de votre Bot, vous appuyez sur **'Reset Token'** et vous le copiez.
***AVERTISSEMENT : Le token n'est a donner à personne. En cas de divulgation, le bot peut être utilisé par n'importe qui possédant le token jusqu'à ce que vous faîtes un reset du token à cet endroit.***
17. Une fois le token copié, vous vous rendez dans le dossier où se trouve les fichiers téléchargés et vous ouvrez le fichier **'.env'**.
18. Vous copiez ensuite votre token entre les guillements **(exemple : BOT_TOKEN='votre_token')**
19. Une fois cela fait, vous pouvez démarrer le bot en ouvrant un CMD (pour Windows) ou un terminal (pour macOS / Linux).
20. Vous vous rendez dans le dossier du projet et marquer la commande **'python3 main.py'**.
(Exemple Windows : Si le fichier se trouve dans le disque local C, alors vous tapez dans le cmd : **dir 'C:'** et vous tapez **'python main.py'**)
(Exemple macOS / Linux : Si le fichier se trouve dans vos téléchargements, vous tapez dans le terminal : **cd '~/Téléchargements'** ou **cd '~/Downloads'** et vous tapez **'python3 main.py'**)
Une fois qu'il est marqué **'Bot is running...'** cela indique que votre bot est en ligne.

Liste des commandes : 
    
    !kick
    Permet de kick un membre
    (Il y a deux arguments : le membre, la raison (facultative))
    Exemples d'utilisation : !kick @abcd
                             !kick @abcd Insultes

    !ban
    Permet de ban un membre
    (Il y a deux arguments : le membre, la raison (facultative))
    Exemples d'utilisation : !ban @abcd
                             !ban @abcd Comportement irrespectueux

    !unban
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

🇬🇧 English

Here's a Discord bot with some interesting features.

# Usage

1. Firstly, you need to install Python.
[To do that, visit this site:] (https://www.python.org/downloads/) and download the latest version suitable for your operating system.

2. Next, you'll need to install another tool called Pip.
[For this, go to the site (Windows):] (https://waytolearnx.com/2020/06/comment-installer-pip-pour-python-sur-windows.html)
[(macOS / Linux):] (https://stacklima.com/comment-installer-pip-dans-macos/)

Furthermore, you'll need to install the **'discord.py'** module to make the bot work.
3. To do this, open a cmd prompt (for Windows) or a terminal (for macOS / Linux) and type the command: **pip install discord.py**

4. [Now, go to the Discord Developer Portal:] (https://discord.com/developers/docs/intro)
5. Log in.
6. Create an application (using the New Application button).
7. Enter your bot's name.
8. Check the box and press Create.
9. You can now add an image to your bot, modify its name, etc.
10. Click on **'Bot'** in the left dropdown menu.
11. Then scroll down to the **'Privileged Gateway Intents'** section and check all three options.
12. Return to the left dropdown menu, click on **'OAuth2'**, and then **'URL Generator'**.
13. In **'Scopes'**, check **'bot'** and **'applications.commands'**.
14. Next, in **'Bot Permissions'**, check **'Administrator'** and retrieve the link to invite the bot to your server.
15. Once done, return to the left dropdown menu and click on **'Bot'**.
16. Under **'TOKEN'**, next to your Bot's logo, click on **'Reset Token'** and copy it.
***WARNING: The token should not be shared with anyone. If disclosed, the bot can be used by anyone with the token until you reset the token at this location.***
17. Once the token is copied, navigate to the folder where the downloaded files are located and open the **'.env'** file.
18. Then paste your token between the quotes (**example: BOT_TOKEN='your_token'**)
19. Once this is done, you can start the bot by opening a CMD prompt (for Windows) or a terminal (for macOS / Linux).
20. Navigate to the project folder and enter the command **'python3 main.py'**.
(Windows example: If the file is located on local disk C, then type in cmd: **dir 'C:'** and type **'python main.py'**)
(macOS / Linux example: If the file is in your downloads folder, type in the terminal: **cd '~/Downloads'** and then **'python3 main.py'**)
When you see **'Bot is running...'**, it means your bot is online.

Lun0xxx :).
