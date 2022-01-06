import hikari
import lightbulb

monke_plugin = lightbulb.Plugin("Monke")


@monke_plugin.command
@lightbulb.command("monke", "monke meme.", aliases=["monkey", "mono", "life"])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def monke(ctx: lightbulb.Context) -> None:
    await ctx.respond("https://www.youtube.com/watch?v=x6ZRNZxNbbw")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(monke_plugin)