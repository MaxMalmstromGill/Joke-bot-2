import discord
import requests
import json


class myClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {client.user}'.format(client))



    async def on_message(self, ctx):
            if ctx.author == client.user:
                return
            elif ctx.content.startswith('make me laugh'):
                await ctx.channel.send('Chuck Norris joke?')
                res = await client.wait_for('message', check=lambda message: ctx.author == message.author)
                if res.content.lower() == ('yes'):
                    async def get_joke(self):
                        response = requests.get(
                            'https://api.chucknorris.io/jokes/random')
                        joke = json.loads(response.text)
                        return(joke['value'])
                    the_joke = await get_joke(self)
                    await ctx.channel.send(the_joke)
                else:
                    await ctx.channel.send('no problem!')


client = myClient()
client.run('OTM1MTM4MDU3MzI4NDI3MDM5.Ye6RLg.QK7Hx4Cjp1LAEjGeQwnKb2pe5vQ')
