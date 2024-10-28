import discord 
from discord.ext import commands
import datetime
from datetime import datetime
import psutil
start_time = datetime.now()
class ahem(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  
  @commands.hybrid_command(aliases=['up'],help="Shows Uptime of the Bot")
  async def uptime(self,ctx):
    current_time = datetime.now()
    uptime_duration = current_time - start_time
    days = uptime_duration.days
    hours, remainder = divmod(uptime_duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_str = f"<a:HeartPoofo:1275760347470626889> Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    await ctx.send(uptime_str)
    
  @commands.hybrid_command(help="checks bot's latency")
  async def ping(self,ctx):
      embed = discord.Embed(color=0x2C2F33)
      embed.set_author(
  name=f"🏓 |...pong! In {int(self.bot.latency * 1000)} ms ",
  icon_url=ctx.author.display_avatar.url)
      await ctx.reply(embed=embed)

  @commands.hybrid_command(help="Sends Help Panel of the Bot.")
  async def help(self,ctx):
       loading_message = await ctx.send(embed=discord.Embed(
       color=0x2f3136,
       description="**<a:HeartPoofo:1275760347470626889> Loading Help menu...**"
       ))
       button = discord.ui.Button(label="Support Server", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUKcmljayByb2xsIA%3D%3D", style=discord.ButtonStyle.link)
       button1 = discord.ui.Button(label="Invite Me", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUKcmljayByb2xsIA%3D%3D", style=discord.ButtonStyle.link)
       embed = discord.Embed(
       color=0x2f3136,
       description=
       "◇Hey, It's Me Legend A Feature Rich Advanced Ticketing Bot. Try Legend Now!\n◇My Prefix is `!`."
       )
       embed.add_field(name='**Bot Commands**',
       value=f"`ticket setup`, `ticket info`, `ticket edit`, `ticket delete`, `ticket reset`, `ticket reopen`, `ticket close`, `ticket transcript`,  `ticket rename`, `ping`, `invite`, `stats`, `uptime`.",
           inline=False)
       view = discord.ui.View()
       view.add_item(button)
       view.add_item(button1)
       embed.set_author(name=f"Help panel",
        icon_url=self.bot.user.display_avatar.url)
       embed.set_thumbnail(url=self.bot.user.display_avatar.url)
       await loading_message.delete()
       await ctx.send(embed=embed, view=view)
  @commands.hybrid_command()
  async def invite(self,ctx):
      embed = discord.Embed(
          title="** <a:HeartPoofo:1275760347470626889> Legend's Invite**<a:HeartPoofo:1275760347470626889> ",
          description=
          "> • **[Invite Me ](https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUKcmljayByb2xsIA%3D%3D)\n> • [Support Server](https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUKcmljayByb2xsIA%3D%3D)**",
          color=0x41eeee)    
      await ctx.send(embed=embed)
  @commands.hybrid_command()
  async def stats(self,ctx):
       """Shows some usefull information about Legend"""
       loading_message = await ctx.send(embed=discord.Embed(
       color=0x2f3136,
       description="**<a:HeartPoofo:1275760347470626889> Fetching Info From Database...**"
       ))
       serverCount = len(self.bot.guilds)
       textchannel = sum(len(guild.text_channels) for guild in self.bot.guilds)
       voicechannel = sum(len(guild.voice_channels) for guild in self.bot.guilds)
       categorichannel = sum(len(guild.categories) for guild in self.bot.guilds)
       total = textchannel + voicechannel + categorichannel
       cached = len(self.bot.users)
       used_memory = psutil.virtual_memory().percent
       cpu_used = str(psutil.cpu_percent())
       shard_count = self.bot.shard_count
       total_members = sum(g.member_count for g in self.bot.guilds
           if g.member_count != None)
       pain = await self.bot.fetch_user(1086533487089172550)
       papa = await self.bot.fetch_user(876413893558284339)
       uts = await self.bot.fetch_user(1188712861510422549)
       boss = await self.bot.fetch_user(1188712861510422549)
       light = await self.bot.fetch_user(926831289649201213)
       button = discord.ui.Button(label="Support Server", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUKcmljayByb2xsIA%3D%3D", style=discord.ButtonStyle.link)
       button1 = discord.ui.Button(label="Invite Me", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUKcmljayByb2xsIA%3D%3D", style=discord.ButtonStyle.link)
       embed = discord.Embed(
       color=0x2f3136,
       description=
       "**Hey, It's Me Legend A Feature Rich Advanced Ticketing Bot. Try Legend Now!**"
       )
       embed.add_field(
       name="**<a:HeartPoofo:1275760347470626889> DEVELOPERS**",
       value=f"[{pain}](https://discord.com/users/1036877996243562516)\n[{papa}](https://discord.com/users/926831289649201213)")
       embed.add_field(
       name="**<a:HeartPoofo:1275760347470626889> TEAM**",
       value=f"[{light}](https://discord.com/users/111291498191949824)\n[{uts}](https://discord.com/users/1112334748656861365)",
       inline=False)
       embed.add_field(name='**Bot Stat(s)**',
       value=f"**→** Total Guilds: **{serverCount} Guilds**\n**→** Total Users: **{total_members} Users | {cached} Cached**\n**→** Channels:\n- Total: **{total} Channels**\n- Text: **{textchannel} Channels**\n- Voice: **{voicechannel} Channels**\n- Categories: **{categorichannel} Channels**",
           inline=False)
       embed.add_field(
       name="**Server(s) Usage**",
       value=
       f"**→** CPU Usage: **{cpu_used}%**\n**→** Memory Usage: **{used_memory}%**",
           inline=False)
       embed.add_field(
       name="**Shard(s)**",
       value=f"**{ctx.guild.shard_id + 1}/{shard_count}**",
           inline=False)
       view = discord.ui.View()
       view.add_item(button)
       view.add_item(button1)
       embed.set_author(name=f"About {self.bot.user.name}",
        icon_url=bot.user.display_avatar.url)
       embed.set_thumbnail(url=self.bot.user.display_avatar.url)
       await loading_message.delete()
       await ctx.send(embed=embed, view=view)
    
async def setup(bot):
  await bot.add_cog(ahem(bot))