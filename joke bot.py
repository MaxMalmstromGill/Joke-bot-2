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
        #svara på rätt person
            if ctx.author == client.user:
                return
            #startar chuck norris skämt genom ::cn command
            elif ctx.content.startswith('::cn'):
                await ctx.channel.send('Chuck Norris joke?, Yes/No')
                chuck = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if chuck.content.lower() == ('yes'):
                    #använder requests för att hämta data från api
                    async def get_joke(self):
                            response = requests.get(
                                'https://api.chucknorris.io/jokes/random')
                            joke = json.loads(response.text)
                            return(joke['value'])
                        #skickar skämtet i discord chatten
                    the_joke = await get_joke(self)
                    await ctx.channel.send(the_joke)
                elif chuck.content.lower() == ('no'):
                        await ctx.channel.send(':(')
              #samma igen men med annan api och en annan command ::ym
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
      
         
           #Hjälp låda, använder embed från discord som har importerats
            elif ctx.content.startswith('::help'):
                embed=discord.Embed(title="Commands for different type of jokes:", color=0x005275)
                embed.add_field(name="Chuck Norris joke", value="::cn", inline=False)
                embed.add_field(name="Knock Knock joke", value="::kk \n Who's there?  -  Who?", inline=False)
                embed.add_field(name="Yo momma joke", value="::ym", inline=False)
                await ctx.channel.send(embed=embed)

            #knock knock skämt, ingen api utan text dokument som används som källa till skämten
            elif ctx.content.startswith('::kk'):
                await ctx.channel.send('Knock knock!')
                res = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if res.content.lower() == ("who's there?") or ("whos there") or ("whos there?") or ("who's there"):

                   #avläser dokumentet anväder random.choice för hämta ett skämt som sedan delas i två genom split, skicka första delen.
                    with open("knockjokes.txt", "r", encoding="utf8") as f:
                        knock_joke_list = f.readlines()
                    joke = random.choice(knock_joke_list).split("*") 
                    who = joke[0] 
                    await ctx.channel.send(who)

                    #skickar andra delen
                    answer = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                    if answer.content.lower() == (f"{who} who?") or ("who?") or ("who"):
                       await ctx.channel.send(joke[1])         

            #Ett till extra hjälp för att påminna om hjälp lådan
            elif ctx.content.startswith(('Joke Bot', 'joke bot', 'Joke bot', 'joke Bot')):
                await ctx.channel.send('If you need any help just send "::help" in the chat!')   
                    

client = myClient()
client.run('OTM1MTM4MDU3MzI4NDI3MDM5.Ye6RLg.QK7Hx4Cjp1LAEjGeQwnKb2pe5vQ')
