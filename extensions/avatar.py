import hikari
import lightbulb

avatar_plugin = lightbulb.Plugin("Avatar")


@avatar_plugin.command
@lightbulb.option(
    "target", "The member to get information about.", hikari.User, required=False
)
@lightbulb.command(
    "avatar", "Get the avatar of a server member.", aliases=["ava", "image", "pfp"]
)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def userinfo(ctx: lightbulb.Context) -> None:
    target = ctx.get_guild().get_member(ctx.options.target or ctx.user)

    if not target:
        await ctx.respond("That user is not in the server.")
        return

    embed = (
        hikari.Embed(
            title=f"{target.display_name}'s Avatar",
            description=f"**Get the full image**\n[click here!]({target.avatar_url or target.default_avatar_url})",
            colour=target.get_top_role().color
        )
        .set_image(target.avatar_url or target.default_avatar_url)
    )

    await ctx.respond(embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(avatar_plugin)
