import os
import discord
import feedparser
from dotenv import load_dotenv
from discord.ext import tasks


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
NEWS_CHANNEL_ID = int(os.getenv('NEWS_CHANNEL_ID')) 

if not TOKEN or not NEWS_CHANNEL_ID:
    raise ValueError("Token do Discord ou ID do Canal não encontrados! Verifique seu arquivo .env")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

NEWS_FEED_URL = "https://g1.globo.com/rss/g1/"

@bot.event
async def on_ready():
    print(f'Logado com sucesso como {bot.user}!')
    print('Iniciando a tarefa de notícias agendadas...')
    send_news.start()
    print('------')

@bot.event
async def on_ready():
    print(f'Logado com sucesso como {bot.user}!')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '!ola':
        await message.channel.send(f'Olá, {message.author.name}!')

    if message.content == '!noticias':
        await message.channel.send("Buscando as últimas notícias do G1...")

        try:
            feed = feedparser.parse(NEWS_FEED_URL)
            
            for entry in feed.entries[:5]:
                embed = discord.Embed(
                    title=entry.title,
                    url=entry.link,
                    description=entry.summary,
                    color=discord.Color.blue()
                )
                embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
                
                await message.channel.send(embed=embed)

        except Exception as e:
            await message.channel.send("Desculpe, ocorreu um erro ao buscar as notícias.")
            print(f"Erro ao processar o feed: {e}")

@tasks.loop(minutes=1)
async def send_news():
    channel = bot.get_channel(NEWS_CHANNEL_ID)
    if not channel:
        print(f"ERRO: Canal com ID {NEWS_CHANNEL_ID} não encontrado.")
        return

    print("Executando tarefa agendada: buscando notícias...")
    try:
        feed = feedparser.parse(NEWS_FEED_URL)

        for entry in feed.entries[:3]:
            embed = discord.Embed(
                title=entry.title,
                url=entry.link,
                description=entry.summary,
                color=discord.Color.dark_red()
            )
            embed.set_author(name="Últimas Notícias do G1")
            await channel.send(embed=embed)
        
        print("Notícias agendadas enviadas com sucesso.")

    except Exception as e:
        print(f"Erro na tarefa agendada: {e}")

async def main():
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())