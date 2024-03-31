# Telegram Bot with Python

This is a simple Telegram bot created using Python and the `telebot` library. The bot provides basic functionality such as responding to commands and sending messages with custom keyboards.

## Clone this repository:  

```
    git clone https://github.com/TheSecondChance/TeleBot.git
```

## Requirements  

You can install the required library using pip:

```
    pip install -r requirements.txt
```

Set up a Telegram bot and obtain the bot token from the BotFather.

Set the bot token as an environment variable:

```
    export BOT_TOKEN=<your_bot_token>
```

## Run Bot

```
    python3 bot.py
```

## Functionality  

`/start:` Displays a welcome message and provides a button to access a web form.  
`/ToRegister:` Displays a custom keyboard with options for registration.  
`/close:` Closes the custom keyboard.  
`Other messages:` Replies with a message indicating that the input is not correct.  


## Customization
Modify the bot's functionality and commands as needed.  
Customize the messages and keyboard options according to your requirements.  
Update the README.md with relevant information about your bot and its usage.  