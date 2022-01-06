import hikari
import lightbulb

sans_plugin = lightbulb.Plugin("Sans")


@sans_plugin.command
@lightbulb.command("sans", "human sans meme.", aliases=["sans humano", "cota", "cototo", "cotota"])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def sans(ctx: lightbulb.Context) -> None:
    await ctx.respond("https://www.youtube.com/watch?v=M3dLsyGKWn8")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(sans_plugin)