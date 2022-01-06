import hikari
import lightbulb

freddy_plugin = lightbulb.Plugin("Freddy")


@freddy_plugin.command
@lightbulb.command("freddy", "rapper freddy meme.", aliases=["fred"])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def freddy(ctx: lightbulb.Context) -> None:
    await ctx.respond("https://www.youtube.com/watch?v=nIsCYSJhiH4")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(freddy_plugin)