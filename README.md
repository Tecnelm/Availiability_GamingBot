
# Discord Bot Availiability 

Dans le cadre d'un projet, j'ai eu besoin de pouvoir récupérer des informations provenant de mon ordinateur principal.
 - Récupération des informations sur le temps d'inactivité de l'ordinateur 
 - Lancement à distance de mon ordinateur

Afin de pouvoir réaliser ces deux fonctionnalités, j'ai utilisé un Ordinateur sous Windows (Client) et un Raspberry PI4 (Serveur).

## Requirement 
 - Ordinateur sous Windows 11 (il ne devrait pas y avoir de problème sous windows 10)
 - Raspberry PI4 ou moins
 - Bot discord crée
 - Python 3

## Discord 
### Création
Afin de pouvoir créer un bot discord, il est nécessaire de [créer un bot](https://discord.com/developers/applications) sur le site développeur de discord 
Par la suite, il faudra récupérer le token permettant de se connecter au bot en question. 
Ensuite inviter le bot en question sur l'un de vos serveurs. :
- Aller dans l'onglet OAuth2/URL Generator de votre bot 
- Sélectionner Bot
- Générer le lien avec les bonnes permissions
- Mettre le lien dans le navigateur et inviter votre bot

**Pour pouvoir interagir avec le bot, il faudra que les utilisateurs aient en commun un serveur avec le bot**

## Serveur 
Installer les requirement avec 
>pip install -r Requirement.txt


### Configuration
```
Discord:  
  token: $token  
  commande:  
    start: "!"  
  cmd:  
	  - "pong"  
	  - "ask"  
	  - "help"  
	  - "start"  
  response:  
    help:  
	  - "!pong."  
	  - "!ask: affiche depuis combien de temps le pc n'est pas en activité."  
	  - "!help: affiche les commandes."  
	  - "!start: démarre le PC."  
  startup: "Démarage de l'ordinateur!"  
  
  ask:  
      available: "l'ordinateur est en inactivité depuis: "  
	  unvailable: "L'ordinateur est actuelement non disponnible!"  
	  switched_off: "L'ordinateur est actuelement éteint"  
	  timeMin: $timeMinAFK  
      commande: "time"  
   pong: "Ping!"  
  
Startup:  
  wol:  
    mac: $mac  
  
Server:  
  port: $port  
  ip: $address
```

### Lancement 
>python3 ./main.py

### Ajouter une commande 
Pour ajouter une commande, rajouter dans le fichier de configuration : "discord: cmd: "cmd_name" "
Rajouter dans response les données que vous avez besoin pour le traitement de votre commande (le mot clef doit être le nom de la commande) 
Rajouter votre commande dans le  la package Discord/Bot.py nommer la fonction à exécuter  **cmd_"cmdName"** et prend comme argument le message. 


### Docker 
#### Build depuis les sources 
> docker build -t "name" .
> docker run "name" --arg ..........
#### Docker compose 
```
version: "3"  
services:  
  discordbot:  
    image: tecnelm/discordbot:latest  
    container_name: botDiscord  
    environment:  
      - TOKEN=""  
      - PORT=
      - ADDRESS=''  
      - MAC=""  
      - TIME_MIN_AFK=  
    network_mode: host  
    restart: unless-stopped
```

## Client
Installer les requirement avec 
>pip install -r Requirement.txt


### Configuration

```
Discord:  
  response:  
    ask:  
      commande: "time"  
Server:  
  port: -  
  ip: "-"
```

### Lancement automatique 

Lancer exécuter (WIN+R) puis rentrer **shell:startup** dans ce fichier copier le raccourci de launch_client_ab.vbs 





