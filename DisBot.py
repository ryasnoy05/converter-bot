import discord
from discord.ext import commands
from parsere import  USD, EUR, GBP, CHF , CAD, AUD, TRY, SGD, UAH, DKK, NOK, SEK, CNY, ETH, LTC, BTC
import os
bot = commands.Bot(command_prefix='v.') #отправляем обратно аргумент
@bot.command()
async def Bitcoin(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 биткоин = {BTC.group(0)} рублей**', color=0x0c0c0c))#await ctx.send(f"1 биткоин = {BTC.group(0)} рублей")
@bot.command()
async def Dollar(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 доллар = {USD} рубл**', color=0x0c0c0c))#await ctx.send(f"1 доллар = {USD} рублей")
@bot.command()
async def Euro(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 евро = {EUR} рублей**', color=0x0c0c0c))#await ctx.send(f"1 евро = {EUR} рублей")
@bot.command()
async def Pound(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 фунт стерлингов = {GBP} рублей**', color=0x0c0c0c))#await ctx.send(f"1 фунт стерлингов = {GBP} рублей")
@bot.command()
async def Franc(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 швейцарский франк = {CHF} рублей**', color=0x0c0c0c))#await ctx.send(f"1 швейцарский франк = {GBP} рублей")
@bot.command()
async def Canadian(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 канадский доллар = {CAD} рублей**', color=0x0c0c0c))#await ctx.send(f"1 канадский доллар = {GBP} рублей")
@bot.command()
async def Australian(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 австралийский доллар = {AUD} рублей**', color=0x0c0c0c))#await ctx.send(f"1 австралийский доллар = {GBP} рублей")
@bot.command()
async def Turkish(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 новая турецкая лира = {TRY} рублей**', color=0x0c0c0c))#await ctx.send(f"1 новая турецкая лира = {GBP} рублей")
@bot.command()
async def Singapore(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 сингапурский доллар = {SGD} рублей**', color=0x0c0c0c))#await ctx.send(f"1 сингапурский доллар = {GBP} рублей")
@bot.command()
async def Ukrainian(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 украинская гривна = {UAH} рублей**', color=0x0c0c0c))#await ctx.send(f"1 украинская гривна = {GBP} рублей")
@bot.command()
async def Danish(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 датская крона = {DKK} рублей**', color=0x0c0c0c))#await ctx.send(f"1 датская крона = {GBP} рублей")
@bot.command()
async def Norwegian(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 норвежская крона = {NOK} рублей**', color=0x0c0c0c))#await ctx.send(f"1 норвежская крона = {GBP} рублей")
@bot.command()
async def Swedish(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 шведская крона = {SEK} рублей**', color=0x0c0c0c))#await ctx.send(f"1 шведская крона = {GBP} рублей")
@bot.command()
async def Yuan(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 китайский юань = {CNY} рублей**', color=0x0c0c0c))#await ctx.send(f"1 китайский юань = {GBP} рублей")
@bot.command()
async def Ethereum(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 эфириум = {ETH.group(0)} рублей**', color=0x0c0c0c))#await ctx.send(f"1 эфириум = {ETH.group(0)} рублей")
@bot.command()
async def Litecoin(ctx):
	await ctx.send(embed = discord.Embed(description = f'**1 лайткоин = {LTC.group(0)} рублей**', color=0x0c0c0c))#await ctx.send(f"1 лайткоин = {LTC.group(0)} рублей")
@bot.command()
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=amount)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует. \n Список команд:\nv.Dollar\nv.Euro\nv.Pound\nv.Bitcoin\nv.Franc\nv.Canadian\nv.Australian\nv.Turkish\nv.Singapore\nv.Ukrainian\nv.Danish\nv.Norwegian\nv.Swedish\nv.Yuan\nv.Ethereum\nv.Litecoin**', color=0x0c0c0c))
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
