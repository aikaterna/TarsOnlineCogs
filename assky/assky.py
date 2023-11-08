import discord
from redbot.core import commands
import random

class AsSky(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def assky(self, ctx):
        # List of about 100 random ASCII emojis
        emojis = [
            "( •_•)>⌐■-■",
            "(⌐■_■)",
            "¯\\_(ツ)_/¯",
            "(͡° ͜ʖ ͡°)",
            "ᕕ(ᐛ)ᕗ",
            "ಠ_ಠ",
            "(╯°□°）╯︵ ┻━┻",
            "(つ°ヮ°)つ",
            "ಠ⌣ಠ",
            "(ง'̀-'́)ง",
            "(ʘ言ʘ╬)",
            "ʘ‿ʘ",
            "(´•  ̮ •`)",
            "( ͡~ ͜ʖ ͡°)",
            "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
            "¯\(°_o)/¯",
            "(¬‿¬)",
            "¯\_(ツ)_/¯",
            "ʕ•ᴥ•ʔ",
            "ᘳᗢᘰ",
            "(ง°ل͜°)ง",
            "ʕ•̀ω•́ʔ✧",
            "(¬‿¬)ﾉ",
            "¯\(°_o)/¯",
            "(ง •̀_•́)ง",
            "ヽ(˃ヮ˂)ノ",
            "ヾ(⌐■_■)ノ",
            "ʘ‿ʘ╬",
            "╚(•⌂•)╝",
            "(ʘ‿ʘ)╯",
            "(づ◡﹏◡)づ",
            "ʕ·ᴥ·ʔ",
            "ʕ•́ᴥ•̀ʔっ",
            "ʘ ͜ʖ ʘ",
            "┬─┬ノ(ಠ_ಠノ)",
            "(ಥ﹏ಥ)",
            "（°o°；）",
            "(ಠ_ಠ)",
            "ಥ_ಥ",
            "(¬‿¬)",
            "(¬‿¬)ﾉ",
            "¯\_(ツ)_/¯",
            "╮(╯▽╰)╭",
            "¯\_(ツ)_/¯",
            "ヽ(⌐■_■)ノ",
            "ヾ(⌐■_■)ノ",
            "¯\(°_o)/¯",
            "(¬‿¬)ﾉ",
            "¯\(°_o)/¯",
            "(ʘ言ʘ╬)",
            "ʘ‿ʘ",
            "(ʘ‿ʘ)╯",
            "ʘ‿ʘ╬",
            "(¬‿¬)",
            "ヽ(˃ヮ˂)ノ",
            "ʘ‿ʘ",
            "ʕ•́ᴥ•̀ʔっ",
            "ヾ(⌐■_■)ノ",
            "(¬‿¬)ﾉ",
            "ʕ•́ᴥ•̀ʔっ",
            "ʘ ͜ʖ ʘ",
            "┬─┬ノ(ಠ_ಠノ)",
            "(⌐■_■)",
            "(ʘ言ʘ╬)",
            "ʕ•̀ω•́ʔ✧",
            "ヽ(⌐■_■)ノ",
            "(ʘ ͜ʖ ʘ)",
            "ʕ•́ᴥ•̀ʔっ",
            "(¬‿¬)",
            "ʕ•́ᴥ•̀ʔ✧",
            "(⌐■_■)",
            "ʕ•̀ω•́ʔ✧",
            "ヽ(⌐■_■)ノ",
            "(¬‿¬)ﾉ",
            "ʕ•ᴥ•ʔ",
            "ᘳᗢᘰ",
            "ʕ•̀ω•́ʔ✧",
            "ᘳᗢᘰ",
            "¯\_(ツ)_/¯",
            "ʘ‿ʘ",
            "(´•  ̮ •`)",
            "╚(•⌂•)╝",
            "¯\(°_o)/¯",
            "(͡° ͜ʖ ͡°)",
            "ʘ ͜ʖ ʘ",
            "(ʘ言ʘ╬)",
            "（°o°；）",
            "ʘ‿ʘ",
            "（°o°；）",
            "( ͡~ ͜ʖ ͡°)",
            "(⌐■_■)",
            "(´•  ̮ •`)",
            "¯\(°_o)/¯",
            "¯\_(ツ)_/¯",
            "ʘ ͜ʖ ʘ",
            "(ʘ ͜ʖ ʘ)",
            "ʘ‿ʘ",
            "╚(•⌂•)╝",
            "ᘳᗢᘰ",
            "¯\_(ツ)_/¯",
            "ʕ•́ᴥ•̀ʔ✧",
            "ʕ•ᴥ•ʔ",
            "(つ°ヮ°)つ",
            "¯\(°_o)/¯",
            "(¬‿¬)",
            "¯\(°_o)/¯",
            "(ง •̀_•́)ง",
            "ヽ(˃ヮ˂)ノ",
            "ヾ(⌐■_■)ノ",
            "ʘ‿ʘ╬",
            "╚(•⌂•)╝",
            "(ʘ‿ʘ)╯",
            "(づ◡﹏◡)づ",
            "ʕ·ᴥ·ʔ",
            "ʕ•́ᴥ•̀ʔっ",
            "ʘ ͜ʖ ʘ",
            "┬─┬ノ(ಠ_ಠノ)",
            "(ಥ﹏ಥ)",
            "(つ°ヮ°)つ",
            "(ง'̀-'́)ง",
            "ಠ⌣ಠ",
            "( ͡~ ͜ʖ ͡°)",
            "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
        ]

        random_emoji = random.choice(emojis)
        await ctx.send(random_emoji)