import discord
import keep_alive
import os
import io
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
from xlist import linkpls
from xlist import namepls
from xlist import sub
from discord.ext import commands
#testing part
import requests, json
import certifi
import ssl
#test end
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
      channel = ctx.author.voice.channel
      voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        
    @commands.command()
    async def test(self, ctx):
        url = requests.get("https://listen.samcloud.com/webapi/station/78063/history/npe?token=cf8d100d2f5e841ecdb8428e14bab72b1b281bfe&format=json&_=1640289432455", verify=False)
        text = url.text
        await ctx.send(text)

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def adr(self, ctx):
      embed=discord.Embed(title="Asia Dream Radio", url='https://asiadreamradio.torontocast.stream/stations/en/index.html', color=0xee2b34)
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/613417127143014520/923469619405127680/c300.png')
      embed.add_field(name="jhits", value="[Japan Hits](https://asiadreamradio.torontocast.stream/stations/japanhitsplayer.html)", inline=False)
      embed.add_field(name="jpop", value="[J-Pop Powerplay](https://asiadreamradio.torontocast.stream/stations/jpowerplayer.html)", inline=False)
      embed.add_field(name="jkawaii", value="[J-Pop Powerplay Kawaii](https://asiadreamradio.torontocast.stream/stations/jkawaiiplayer.html)", inline=False)
      embed.add_field(name="jrock", value="[J-Rock PowerPlay](https://asiadreamradio.torontocast.stream/stations/jrockplayer.html)", inline=False)
      embed.add_field(name="jclub", value="[J-Club Powerplay HipHop](https://asiadreamradio.torontocast.stream/stations/jclubplayer.html)", inline=False)
      embed.add_field(name="jsakura", value="[J-Pop Sakura](https://asiadreamradio.torontocast.stream/stations/natsukashiiplayer.html)", inline=False)
      embed.add_field(name="jazz", value="[Jazz Club Bandstand](https://asiadreamradio.torontocast.stream/stations/jazzbandplayer.html)", inline=False)
      embed.add_field(name="jazzs", value="[Jazz Sakura](https://asiadreamradio.torontocast.stream/stations/jazzsakuraplayer.html)", inline=False)
      embed.add_field(name="jxmas", value="[J-Pop Christmas Radio](https://asiadreamradio.torontocast.stream/stations/christmasplayer.html)", inline=False)
      await ctx.send(embed=embed)

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, args ):
      channel = ctx.author.voice.channel
      voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
      args = args.lower()

      if voice == None:
        await channel.connect()
        # check voice channel
      if args in sub :
        i = sub.index(args)
        async with aiohttp.ClientSession() as session:
          async with session.get(linkpls[i]) as resp:
            if resp.status != 200:
                  return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.send('ccplay' , file=discord.File(data, namepls[i]))
      else :
        await ctx.send("-_- check list `xxadr`")      
    
    @commands.command()
    async def test(self , ctx , *, args ):
      async with aiohttp.ClientSession() as session:

        webhook = Webhook.from_url('https://discord.com/api/webhooks/923682101847552011/ZNWvzljIMCv3pVsqXsjFZZykzJKJBkQz_8lPeGA5x2BQTQO-lB1_DyILxsc1-TwSGrOS', adapter=AsyncWebhookAdapter(session))
        await webhook.send(args , username=ctx.author.name, avatar_url=ctx.author.avatar_url)
            
    @commands.command()
    async def ping(self , ctx ):
      await ctx.send(f'Pong! In {round(bot.latency * 1000)}ms')


bot = commands.Bot(command_prefix=("xx"), case_insensitive=True)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))

keep_alive.keep_alive()
bot.add_cog(Music(bot))
bot.run(os.getenv("TOKEN"))
