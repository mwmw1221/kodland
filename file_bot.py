import discord,random,os
from discord.ext import commands
import request_addon as rq
import AI

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sigma(ctx):
    await ctx.send("🗿"*random.randint(1,100))

@bot.command()
async def mem(ctx):
    with open('images/img_'+str(random.randint(1,3))+'.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
    # Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def duck(ctx):
    image_url = rq.get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def memduży(ctx):
    await ctx.send("Proszę czekać...")
    file = random.choice(os.listdir('memes'))
    with open('memes/'+file, 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
    # Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def ai(ctx, text):
    await ctx.send("Proszę czekać, generowanie...")
    airequest = AI.ask(text)
    await ctx.send(airequest)

@bot.command()
async def rickroll(ctx, member: discord.Member):
    try:
        rickroll_url = "https://bit.ly/3BlS71b"
        await member.send(f"Cześć {member.name}! Mam coś dla Ciebie: {rickroll_url}")
        await ctx.send(f"Rickroll wysłany do {member.mention}!")
    except discord.Forbidden:
        await ctx.send(f"Nie mogę wysłać wiadomości do {member.mention}, ma wyłączone wiadomości prywatne.")
    except Exception as e:
        await ctx.send(f"Coś poszło nie tak: {e}")

bot.run("erm no.")
