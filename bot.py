import os
import discord
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
# Pega o token do bot a partir das variáveis de ambiente
TOKEN = os.getenv('DISCORD_TOKEN')

# Verifica se o token foi carregado
if not TOKEN:
    raise ValueError("Token do Discord não encontrado no arquivo .env!")

# Intents são as permissões que o bot precisa para acessar certos eventos
intents = discord.Intents.default()
# Habilita a permissão para ler o conteúdo das mensagens
intents.message_content = True

# Cria a instância do bot com as intents configuradas
client = discord.Client(intents=intents)

# O evento 'on_ready' é chamado quando o bot se conecta com sucesso ao Discord
@client.event
async def on_ready():
    # Imprime uma mensagem no terminal
    print(f'Bot conectado como {client.user}')
    print('------')

# O evento 'on_message' é chamado toda vez que uma mensagem é enviada em um canal
@client.event
async def on_message(message):
    # Ignora mensagens enviadas pelo próprio bot para evitar loops infinitos
    if message.author == client.user:
        return

    if message.content.startswith('!ola'):
        # Envia uma resposta no mesmo canal onde o comando foi digitado
        await message.channel.send('Olá!')

# O 'run()' inicia o bot e o mantém rodando até parar o script
client.run(TOKEN)