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
    if message.content == "/about":
        await message.channel.send(" :thumbsup: This Bot Is In Devlopment Actually Created By Ben.py #5021 ")

    elif message.content == "/hello":
		    await message.channel.send(" :v: Hey There I Am Your Python Personal Assistant")

    elif message.content == "/what is python":
		    await message.channel.send(" :book: Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation.")

    elif message.content == "/what is if else statement":
		    await message.channel.send(" :book: ")    
#Use Bot Token
bot.run("Use_your_own")

