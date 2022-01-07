import hikari
import lightbulb

help_plugin = lightbulb.Plugin("Help")

HELP_MESSAGE = """
Commands Available:
`avatar` - Gives the avatar of a certain user. | ,avatar <target>
`fun` - Returns a meme or an animal fact | ,fun meme or ,fun animal
`help` - Shows you an overview of the bot commands. | ,help
`info` - Returns information of a certain user. | ,info <target>
`mod` - Purges an x amount of messages. | ,purge <amount>
`monke` - Links the best video ever. | ,monke
`roles` - Returns an embed with the roles of a certain user | ,roles <target>
"""

@help_plugin.command
@lightbulb.command("help", "Help command that shows the function of every command.", aliases=["hp", "ayuda", "commands", "cmds", "cmd", "command"])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context) -> None:

    embed = hikari.Embed(
        title="General commands information",
        description=HELP_MESSAGE,
    )
    await ctx.respond(embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(help_plugin)