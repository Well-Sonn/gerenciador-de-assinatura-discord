import discord
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Inicia o bot de Discord'

    def handle(self, *args, **options):
        # É necessário configurar os 'intents' para que o bot possa receber eventos específicos
        intents = discord.Intents.default()
        intents.message_content = True  # Ativa o intent para ler conteúdo de mensagens

        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            self.stdout.write(self.style.SUCCESS(f'Bot logado como {client.user}'))

        @client.event
        async def on_message(message):
            # Ignora mensagens do próprio bot para evitar loops
            if message.author == client.user:
                return

            # Comando de teste simples
            if message.content.startswith('!ping'):
                await message.channel.send('Pong!')
                self.stdout.write(f'Comando !ping executado por {message.author}')

        # Pega o token a partir das configurações do Django
        TOKEN = settings.DISCORD_BOT_TOKEN
        if not TOKEN:
            self.stdout.write(self.style.ERROR('Token do Discord não encontrado nas configurações.'))
            return

        self.stdout.write("Iniciando o bot...")
        client.run(TOKEN)