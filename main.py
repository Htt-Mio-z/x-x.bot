import discord
import keep_alive
import os
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
      channel = ctx.author.voice.channel
      await channel.connect()
    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def jhits(self, ctx):
        await ctx.send('ccplay https://cdn.discordapp.com/attachments/613417127143014520/923072627818496010/Japan_Hits.pls')

    @commands.command()
    async def jclub(self, ctx):
        await ctx.send('ccplay https://cdn.discordapp.com/attachments/613417127143014520/923072627973689344/J-Club_Powerplay_HipHop.pls')
    
    @commands.command()
    async def jkawaii(self, ctx):
        await ctx.send('ccplay https://cdn.discordapp.com/attachments/613417127143014520/923072628313432064/J-Pop_Powerplay_Kawaii.pls')
    
    @commands.command()
    async def jpop(self, ctx):
        await ctx.send('ccplay https://cdn.discordapp.com/attachments/613417127143014520/923072628485410927/J-Pop_Powerplay.pls')
    
    @commands.command()
    async def jsakura(self, ctx):
        await ctx.send('ccplay https://cdn.discordapp.com/attachments/613417127143014520/923072628657356811/J-Pop_Sakura.pls')
    
    @commands.command()
    async def jrock(self, ctx):
        await ctx.send('ccplay https://cdn.discordapp.com/attachments/613417127143014520/923072628846112788/J-Rock_PowerPlay.pls')      
    
    @commands.command()
    async def jazz(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/613417127143014520/923477857622171648/Jazz_Club_Bandstand.pls')      
    
    @commands.command()
    async def jazzs(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/613417127143014520/923477857823502396/Jazz_Sakura.pls')        
    
    @commands.command()
    async def jxmas(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/613417127143014520/923477858012233748/J-Pop_Christmas_Radio.pls')    

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



bot = commands.Bot(command_prefix=("xx"), case_insensitive=True)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))

keep_alive.keep_alive()
bot.add_cog(Music(bot))
bot.run(os.getenv("TOKEN"))
