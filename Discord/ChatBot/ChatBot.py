import discord
import random
import json
import requests


class Responses:

    

    # Get Message from user and return a string
    def GetMessage(Message: str) -> str:


        # Set ProcessedMessage to user input
        ProcessedMessage = Message.lower()


        # If user input hello return Hey There
        if ProcessedMessage == 'hello':
            return "Hey There!"
        
        # If user input roll dice return random number 1-6
        if Message == 'roll dice':
            return str(random.randint(1,6))
        
        # If user input !help return help message
        if ProcessedMessage == '!help':
            return '`This is a help message that you can modify`'

        # If User doesn't type anything return: 
        else:
            return None

    

    
class Bot:

    async def SendMessage(Message, UserMessage, PrivateMessage):
        try:
            Response = Responses.GetMessage(UserMessage)
            await Message.author.send(Response) if PrivateMessage else await Message.channel.send(Response)

        except:
            Responses.GetMessage(UserMessage)

    def RunDiscordBot():
        TOKEN = 'MTA0NzA2OTg4MTg1NTYzOTU4Mg.GsVErk.tEgtfDW1X4dBK4f2OevVnSSrf4aUbTpcQNcAnM'
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        # When Bot is live
        @client.event
        async def on_ready():
            print(f'{client.user} is now running!')
    
        # When a message is typed
        @client.event
        async def on_message(Message):
            if Message.author == client.user:
                return

            # Defines Variable
            Username = str(Message.author)
            UserMessage = str(Message.content)
            Channel = str(Message.channel)


            # Prints detail to terminal
            print(f'{Username} said: "{UserMessage}" in: {Channel}')


            # If user Enters ?
            if UserMessage[0] == '?':

                # Remove question mark 
                UserMessage = UserMessage[1:]

                # Output message in private dm
                await Bot.SendMessage(Message, UserMessage, PrivateMessage = True)

            else:

                # Output message in channel
                await Bot.SendMessage(Message, UserMessage, PrivateMessage = False)
        
        # Run Client Bot
        client.run(TOKEN)

# Run Class
Bot.RunDiscordBot()


        

