# Discord Bot Plan


## What Is The System And How Does it Work?
A general purpose server management bot with a web dashboard. It will help organise and moderate the server. It will also add serveral utilites to users i.e find youtube videos, play music, search for images etc. Functionality can be customised through the dashboard as part of the bot's website.
### Problems to Fix:
TBD
## Who is Going to Use it?
The bot will be used by discord admins, moderators and users in a server and will have various uses for each. admins will assign alerts and specific uses for the bot on the dashboard, moderators will used commands to maintain the server and users will have tools and games to use in the server.
### User:
TBD
### Admin:
TBD
## What Needs to be Added for the Initial Build
 
### Moderation:
- Kick users
- ban/unban users
- softban users
- clear messages
- mute user from voice and text chat
- ban specific links
- have cooldown periods to avoid spam
- Have a banned word filter and warn users
- Record audio as an MP3

### Admin:
- Create new roles
- auto assign roles to new users
- remove roles from users
- log bans, warnings, and kicks
- allow banned or warned users to appeal
- disable a command
- send message to kicked/banned users
- edit join and leave message 
### User:
Utilities:
- Search for Youtube channels and videos by name
- Alerts for new videos from followed Youtube channels
- Alert for new streams from followed Twitch streamers
- Alert for new tweets from followed Twitter profiles
- Display a welcome message and rules to new server users
- Simple games with leaderboards
Games:
- Coin flip 
- Blackjack
- image game
### Website:
- add the bot to a server
- list of commands 
- contact info
- social media links
## What is the User Going to See When They Log in?
### Graphical Info?
Web Dashboard from website.
### Commands
- !help: Displays all the commands
- !hellopablo: Pablo quacks at you
- !clear(number of posts): deletes previous number of posts (the default is 2, the clear command and the previous post).
### Admin?
TBD
## Tech Stack:
### Discord Bot:
#### Back-end:
- Python
  - Modules:
   	- [Discord.py](https://pypi.org/project/discord.py/), [Discord.py docs](https://discordpy.readthedocs.io/en/latest/index.html#)
  - APIs:
  	- [Youtube API](https://developers.google.com/youtube/v3), [Github](https://github.com/googleapis/google-api-python-client)
		
#### Database:
TBD
#### Hosting:
TBD
#### Ideas for website:		
- [Dyno](https://dyno.gg/bot)
- [Rythm](https://rythm.fm/)
- [Vexera](https://vexera.io/docs/gs) 
- [Dankmemer](https://dankmemer.lol/)
- [Mee6](https://mee6.xyz/)
- [Maki](https://maki.gg/)
- [Nano](https://nanobot.pw/index.html)
- [More Bots here](https://bots.ondiscord.xyz/)
- [Top.gg](https://top.gg/)
- [Discord.bots](https://discord.bots.gg/)

### Useful Infomation:
- [Youtube Video on Moderation Bots](https://www.youtube.com/watch?v=SwaGOfAKoT0)
- [List of Moderation Bots](https://droplr.com/how-to/productivity-tools/top-5-discord-moderation-bots-to-keep-your-server-safe/)
- [Oauth2 For Adding Discord Login to Website](https://discord.com/developers/docs/topics/oauth2)
- [A video on adding oauth2 to a website in Flask (How i'd make it)](https://www.youtube.com/watch?v=xiYEKe1Q1MI)
- [Discord Moderation](https://discord.com/moderation)
		
