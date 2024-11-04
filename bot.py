import discord,random # type: ignore
import bot_extensions as ext
import emoji as emotki
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("$emoji"):
        emoji = random.choice(emotki.all.emojis)
        await message.channel.send(emoji)
    elif message.content.startswith("$pass "):
        num = str(message.content).replace("$pass ", "")
        if num.isnumeric():
            await message.channel.send(ext.password.get(num))
        else:
            await message.channel.send("Nieprawidłowy argument.")
    else:
        await message.channel.send(message.content)

client.run("MTMwMTIwNDc4NzYwMTIxNTU1OQ.GWTCim.5yE6Sm0hgKBCuxwN3yj9se8tJavPQ_6HuNzQSk")