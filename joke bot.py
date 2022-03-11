import discord
import requests
import json
import random


class myClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {client.user}'.format(client))



    async def on_message(self, ctx):
            if ctx.author == client.user:
                return
            elif ctx.content.startswith('::cn'):
                await ctx.channel.send('Chuck Norris joke?')
                chuck = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if chuck.content.lower() == ('yes'):
                    async def get_joke(self):
                            response = requests.get(
                                'https://api.chucknorris.io/jokes/random')
                            joke = json.loads(response.text)
                            return(joke['value'])
                    the_joke = await get_joke(self)
                    await ctx.channel.send(the_joke)
            elif ctx.content.startswith('::ym'):
                await ctx.channel.send('Yo momma joke?')
                momma = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if momma.content.lower() == ('yes'):
                    async def yomomma(self):
                            response = requests.get(
                                'https://api.yomomma.info/')
                            yo = json.loads(response.text)
                            return(yo['joke'])
                    the_momma = await yomomma(self)
                    await ctx.channel.send(the_momma)


    
    
            elif ctx.content.startswith('::kk'):
                await ctx.channel.send('Knock knock!')
                res = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if res.content.lower() == ("who's there?"):

                   
                    with open("knockjokes.txt", "r", encoding="utf8") as f:
                        knock_joke_list = f.readlines()
                    joke = random.choice(knock_joke_list).split("*") 
                    who = joke[0] #the who is the first element of the list
                    await ctx.channel.send(who)


                    answer = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                    if answer.content.lower() == (f"{who} who?".lower()):
                        await ctx.channel.send(joke[1]) #sending second element in joke sublist
                    
                    

client = myClient()
client.run('OTM1MTM4MDU3MzI4NDI3MDM5.Ye6RLg.QK7Hx4Cjp1LAEjGeQwnKb2pe5vQ')
