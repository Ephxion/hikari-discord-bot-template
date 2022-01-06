# Imports
import os
import hikari
import aiohttp
import dotenv
import lightbulb

# Loading the .env file
dotenv.load_dotenv()

# Functions
from utils.functions import array_to_string, codestring

# Initialize the bot
bot = lightbulb.BotApp(os.environ["TOKEN"], 
prefix=",", 
help_slash_command=True,
default_enabled_guilds=(int(os.environ["GUILD_ID_N"]), int(os.environ["GUILD_ID_M"])),
case_insensitive_prefix_commands=True,
intents=hikari.Intents.ALL
)

@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()

@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    await bot.d.aio_session.close()

@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("Command restricted to bot owner only.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    elif isinstance(exception, lightbulb.NotEnoughArguments):
        args_missing = []
        for option in exception.missing_options:
            args_missing.append(
                f'{codestring(f"{option.name}: {option.arg_type}")}')

        await event.context.respond(f'Command invocation is missing one or more required arguments.\n- Missing arguments: {array_to_string(array=args_missing, iterable=", ")}.')
    elif isinstance(exception, lightbulb.CommandNotFound):
        return
    else:
        raise exception

@bot.command
@lightbulb.command("ping", description="The bot's ping")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")


bot.load_extensions_from("./extensions/", must_exist=True)

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

bot.run()