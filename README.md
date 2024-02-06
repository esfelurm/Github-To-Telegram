# Github To Telegram

Have a backup of GitHub projects in your channel with this robot! 

The robot is upgradable! 

`If you live in Iran and run on your system, use a valid VPN!`


The job of the robot is to find the projects related to the specified TOPIC and then send it to the Telegram channel. 

## Options

- Remove duplicate posts
- Ability to screenshot from the GitHub page (With 2 sites)
- Download the README.md file of the projects (optional)
- Get the source code of the project in the form of a zip file (optional)
- Translation of project descriptions into Persion
- Get complete project information 


## Screen Shot

<img src="https://github.com/esfelurm/Github-To-Telegram/assets/104654028/1720fa9e-515c-4873-9795-368036ed02b7">


## Sample 

<img src="https://github.com/esfelurm/Github-To-Telegram/assets/104654028/4b44ed4b-0324-4c51-83e9-fdb89c567871">


# How To work

How to work: 
In order to publish projects related to a topic in your channel, you must use the following command :
/change [name topic] [number] [OK/NO] [OK/NO] 
The first parameter is the TOPIC name The second parameter is the number of projects you want to send The third parameter is for whether you want the readme.md file of the repositories to be sent or not The last parameter is the same as the third parameter, with the difference that it sends the source code of the project instead of the readme.md file 

Example : ```/change DDOS 10 OK OK```

## Install

Tested on Python versions: 3.8.3 , 3.11.6

```
git clone https://github.com/esfelurm/Github-To-Telegram
cd Github-To-Telegram
[SET FILE Github-To-Telegram.py]
Running on a server or system: python Github-To-Telegram.py
```

# Setting

```
admin_id = 'Admin numeric ID'
telegram_bot_token = "Token Bot"
telegram_channel_id = "ID Channel (ex : @esfelurm)"
Id_bot = "Username Bot : (ex : @esfelurm_bot)"
```
