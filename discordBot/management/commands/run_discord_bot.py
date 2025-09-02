import os
import discord
from django.core.management.base import BaseCommand
from django.conf import settings
import asyncio
from discord.ext import commands

class Command(BaseCommand):
    help = 'Iniciando o bot do Discord'

    def handle(self, *args, **options):

        asyncio.run(self.main())

    async def main(self):
        # É necessário configurar os 'intents' para que o bot possa receber eventos específicos
        intents = discord.Intents.default()
        intents.message_content = True  # Ativa o intent para ler conteúdo de mensagens
        intents.members = True

        aliha = commands.Bot(command_prefix='!', intents=intents)
            
        cogs_dir = os.path.join(settings.BASE_DIR, 'discordBot', 'cogs')
        for filename in os.listdir(cogs_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                cog_path = f'discordBot.cogs.{filename[:-3]}'
                try:
                    await aliha.load_extension(cog_path)
                    self.stdout.write(self.style.SUCCESS(f'Cog {filename} is loaded.'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Falha ao carregar o cog "{filename[:-3]}": {e}'))
                    
        #Pega o token a partir das configurações do Django
        TOKEN = settings.DISCORD_BOT_TOKEN
        if not TOKEN: 
            self.stdout.write(self.style.ERROR('token não encontrado'))
            return
        
        self.stdout.write("iniciando o bot do discord")        
        await aliha.start(TOKEN)