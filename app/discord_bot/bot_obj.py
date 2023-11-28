import discord
from discord.ext import commands

class Combot(commands.Bot):
    def __init__ (self, command_prefix='!'):
        super().__init__(command_prefix=command_prefix)

    @self.event
    async def on_ready():
        print(f"{self.user} initialization... ready to mis-input perma")

    @self.command(name='hello', help='Greet the user')
    async def hello(ctx):
        await ctx.send(f"Hello {ctx.author.name}!")

    def run_bot(self, token):
        self.run(token)
