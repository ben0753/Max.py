import discord
bot = discord.Client()

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("Max_py is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.content == "/hello":
		await message.channel.send("Hey There I Am Your Python Personal Assistant")
    
#Use Bot Token
bot.run("your_bot_token_not_mine")
