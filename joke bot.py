import discord
import requests
import json
import random


client = discord.Client()


class myClient(discord.Client):
    async def on_ready(self):
   #så man vet att den är inloggad
        print(f'Logged in as {client.user}'.format(client))
        
    async def on_message(self, ctx):
            if ctx.author == client.user:
                return
            elif ctx.content.startswith('::cn'):
                await ctx.channel.send('Chuck Norris joke?, Yes/No')
                chuck = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if chuck.content.lower() == ('yes'):
                    async def get_joke(self):
                            response = requests.get(
                                'https://api.chucknorris.io/jokes/random')
                            joke = json.loads(response.text)
                            return(joke['value'])
                    the_joke = await get_joke(self)
                    await ctx.channel.send(the_joke)
                elif chuck.content.lower() == ('no'):
                        await ctx.channel.send(':(')
            elif ctx.content.startswith('::ym'):
                await ctx.channel.send('Yo momma joke?, Yes/No')
                momma = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if momma.content.lower() == ('yes'):
                    async def yomomma(self):
                            response = requests.get(
                                'https://api.yomomma.info/')
                            yo = json.loads(response.text)
                            return(yo['joke'])
                    the_momma = await yomomma(self)
                    await ctx.channel.send(the_momma)
                elif momma.content.lower() == ('no'):
                        await ctx.channel.send(':(')
        
         
           
            elif ctx.content.startswith('::help'):
                embed=discord.Embed(title="Commands for different type of jokes:", color=0x005275)
                embed.add_field(name="Chuck Norris joke", value="::cn", inline=False)
                embed.add_field(name="Knock Knock joke", value="::kk \n Who's there?  -  Who?", inline=False)
                embed.add_field(name="Yo momma joke", value="::ym", inline=False)
                await ctx.channel.send(embed=embed)


            elif ctx.content.startswith('::kk'):
                await ctx.channel.send('Knock knock!')
                res = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if res.content.lower() == ("who's there?") or ("whos there") or ("whos there?") or ("who's there"):

                   
                    with open("knockjokes.txt", "r", encoding="utf8") as f:
                        knock_joke_list = f.readlines()
                    joke = random.choice(knock_joke_list).split("*") 
                    who = joke[0] 
                    await ctx.channel.send(who)


                    answer = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                    if answer.content.lower() == (f"{who} who?") or ("who?") or ("who"):
                       await ctx.channel.send(joke[1])         


            elif ctx.content.startswith(('Joke Bot', 'joke bot', 'Joke bot', 'joke Bot')):
                await ctx.channel.send('If you need any help just send "::help" in the chat!')   
                    

client = myClient()
client.run('OTM1MTM4MDU3MzI4NDI3MDM5.Ye6RLg.QK7Hx4Cjp1LAEjGeQwnKb2pe5vQ')
