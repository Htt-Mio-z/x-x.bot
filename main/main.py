import discord
import keep_alive
import os
import io
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
import requests, json
#load json
import json
xlist = open('main/xlist.json')
x = json.load(xlist)
# --
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        if voice == None:
            await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def adr(self, ctx):
        embed = discord.Embed(
            title="Asia Dream Radio",
            url="https://asiadreamradio.torontocast.stream/stations/en/index.html",
            color=0xEE2B34,
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/613417127143014520/923469619405127680/c300.png"
        )
        embed.add_field(
            name="jhits",
            value="[Japan Hits](https://asiadreamradio.torontocast.stream/stations/japanhitsplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jpop",
            value="[J-Pop Powerplay](https://asiadreamradio.torontocast.stream/stations/jpowerplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jkawaii",
            value="[J-Pop Powerplay Kawaii](https://asiadreamradio.torontocast.stream/stations/jkawaiiplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jrock",
            value="[J-Rock PowerPlay](https://asiadreamradio.torontocast.stream/stations/jrockplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jclub",
            value="[J-Club Powerplay HipHop](https://asiadreamradio.torontocast.stream/stations/jclubplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jsakura",
            value="[J-Pop Sakura](https://asiadreamradio.torontocast.stream/stations/natsukashiiplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jazz",
            value="[Jazz Club Bandstand](https://asiadreamradio.torontocast.stream/stations/jazzbandplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jazzs",
            value="[Jazz Sakura](https://asiadreamradio.torontocast.stream/stations/jazzsakuraplayer.html)",
            inline=False,
        )
        embed.add_field(
            name="jxmas",
            value="[J-Pop Christmas Radio](https://asiadreamradio.torontocast.stream/stations/christmasplayer.html)",
            inline=False,
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["p"])
    async def play(self, ctx, *, args):
        channel = ctx.author.voice.channel
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        args = args.lower()

        if voice == None:
            await channel.connect()
            # check voice channel
        if args in x[0]['sub']:
            i = x[0]['sub'].index(args)
            async with aiohttp.ClientSession() as session:
                async with session.get(x[0]['linkpls'][i]) as resp:
                    if resp.status != 200:
                        return await ctx.send("Could not download file...")
                    data = io.BytesIO(await resp.read())
                    await ctx.send("ccplay", file=discord.File(data, x[0]['namepls'][i]))
        else:
            await ctx.send("-_- check list `xxadr`")

    @commands.command(aliases=["cs"])
    async def currentsong(self, ctx, *, args):
        args = args.lower()
        if args in x[0]['sub']:
            i = x[0]['sub'].index(args)
        url = requests.get(x[0]['cslink'][i], verify=False)
        text = url.text
        cs = json.loads(text)
        songtitle = cs["m_Item2"]["Title"]
        songpic = cs["m_Item2"]["Picture"]
        artist = cs["m_Item2"]["Artist"]
        timestamp = cs["m_Item2"]["Duration"]  # need converting -_-
        embed = discord.Embed(title=songtitle , url="https://www.google.com/search?q=" + songtitle.replace(' ', '+'))
        embed.set_author(name=artist , url="https://www.google.com/search?q=" + artist.replace(' ', '+'))
        embed.set_thumbnail(url=songpic)
        embed.set_footer(text=timestamp)
        await ctx.send(embed=embed)

    @commands.command()
    async def test(self, ctx, *, args):
        async with aiohttp.ClientSession() as session:

            webhook = Webhook.from_url(
                "https://discord.com/api/webhooks/923682101847552011/ZNWvzljIMCv3pVsqXsjFZZykzJKJBkQz_8lPeGA5x2BQTQO-lB1_DyILxsc1-TwSGrOS",
                adapter=AsyncWebhookAdapter(session),
            )
            await webhook.send(
                args, username=ctx.author.name, avatar_url=ctx.author.avatar_url
            )

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! In {round(bot.latency * 1000)}ms")


bot = commands.Bot(command_prefix=("xx"), case_insensitive=True)


@bot.event
async def on_ready():
    print("Logged in as {0} ({0.id})".format(bot.user))


keep_alive.keep_alive()
bot.add_cog(Music(bot))
bot.run(os.getenv("TOKEN"))
