from datetime import datetime

import hikari
import lightbulb

roles_plugin = lightbulb.Plugin("Roles")


@roles_plugin.command
@lightbulb.option(
    "target", "The member to get information about.", hikari.User, required=False
)
@lightbulb.command(
    "roles", "Get the roles of a server member.", aliases=["rol", "role", "rangos", "rango"]
)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def roles(ctx: lightbulb.Context) -> None:
    target = ctx.get_guild().get_member(ctx.options.target or ctx.user)

    if not target:
        await ctx.respond("That user is not in the server.")
        return

    roles = (await target.fetch_roles())[1:]  # All but @everyone

    embed = (
        hikari.Embed(
            title=f"{target.display_name}'s Roles",
            colour=target.get_top_role().color,
        )
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.avatar_url or ctx.member.default_avatar_url,
        )
        .set_thumbnail(target.avatar_url or target.default_avatar_url)
        .add_field("Top Role", target.get_top_role().mention, inline=False,
        )
        .add_field(
            "Roles",
            ", ".join(r.mention for r in roles),
            inline=False,
        )
    )

    await ctx.respond(embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(roles_plugin)