import discord
import flask
from keep_alive import keep_alive

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
        await message.channel.send(
            ":book: Python is an interpreted, high-level and general-purpose programming language. Python's design "
            "philosophy emphasizes code readability with its notable use of significant indentation.")

    elif message.content == "/what is if else statement":
        await message.channel.send(
            ":book:`Python if...else Statement`The if..else statement evaluates test expression and will execute the "
            "body of if only when the test condition is True . If the condition is False , the body of else is "
            "executed. Indentation is used to separate the blocks.for example see this website "
            "https://www.w3schools.com/python/python_conditions.asp ")

    elif message.content == "/what is print statement":
        await message.channel.send(
            "The print() function prints the given object to the standard output device (screen) or to the text stream file.")

    elif message.content == "/contribute":
        await message.channel.send(":sunglasses: https://replit.com/join/ylhemcew-pianolearnersro")

    elif message.content == "/hello":
        await message.channel.send(" :v: Hey There I Am Your Python Personal Assistant")

    elif message.content == "/hi":
        await message.channel.send(" :v: Hey There I Am Your Python Personal Assistant")

    elif message.content == "/thanks":
        await message.channel.send(" :grinning: your welcome")

    elif message.content == ":dog: yay":
        await message.channel.send(" :dog: yay")

    elif message.content == "/SPAM Ethan.py":
        await message.channel.send(
            " IT WILL SPAM ETHAN 20 TIMES!!!@Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.py @Ethan.pY ")

    elif message.content == "/who is Max":
        await message.channel.send(" HE IS A GOOD DOGEE OG Ben.py")

    elif message.content == "/who is max":
        await message.channel.send(" HE IS A GOOD DOGO OF Ben.py")

    # Use Bot Token


bot.run("use ur own")
keep_alive()
