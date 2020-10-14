import os
from dotenv import load_dotenv

from discord.ext import commands

import pydealer

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=';')



players = {}

deck = pydealer.Deck()
#deck.shuffle()
discard_pile = pydealer.Stack()



@bot.command(name='ingame', help='returns if user in game')
async def in_game(ctx):
    #print(ctx.author, client.user)
    await ctx.send(str(ctx.author) in players)

@bot.command(name='table', help='prints the game state')
async def table(ctx):
    if len(discard_pile) > 0:
        await ctx.send(str(len(deck)) + " cards in deck, " + str(len(discard_pile)) + "cards in discard, faceup:" + str(discard_pile[0]) )
    else:
        await ctx.send(str(len(deck)) + " cards in deck, 0 cards in discard" )

        
    await ctx.send('\n'.join( [str(player)+': '+str(players[player][1]) + "+ " + str(len(players[player][0])) + ' facedown cards' for player in players] ))


@bot.command(name='addme', help='adds player to game')
async def add_me(ctx):
    #await ctx.send('testing testing')
    if str(ctx.author) in players:
        await ctx.send('already in game')
    else:
        players[str(ctx.author)] = [[],[]]
        await ctx.send(str(ctx.author) + ' added to game')
        await table(ctx)


@bot.command(name='hand', help='PMs you your hand')
async def hand(ctx):
    await ctx.author.send(str(players[str(ctx.author)]))

@bot.command(name='draw', help='draws a card from discard or deck')
async def draw(ctx, num: int, pile: str):
    if pile == 'discard':
        temp = list(discard_pile.deal(num))
    else: #LAZY
        temp = list(deck.deal(num))

    
    #players[str(ctx.author)][0] += [temp[i] for i in range(len(temp))]
    players[str(ctx.author)][0] += temp
    await hand(ctx)

@bot.command(name='discard', help='moves a card to discard pile')
async def discard(ctx, which: str, ind):
    #which is 'hand' or 'table'
    if which == 'hand':
        which = 0
    elif which == 'table':
        which = 1
    else:
        ctx.send('error')
        return
    
    if ind == 'all':
        for card in players[str(ctx.author)][which]:
            discard_pile.add(card)
        players[str(ctx.author)][which] = []

    else:
        disc = players[str(ctx.author)][which][int(ind)]
        players[str(ctx.author)][which].remove(disc)
        discard_pile.add(disc)


    await table(ctx)

    


    
@bot.command(name='play', help='moves a card to table')
async def play(ctx, ind: int):
    disc = players[str(ctx.author)][0][ind]
    players[str(ctx.author)][0].remove(disc)
    players[str(ctx.author)][1].append(disc)
    await table(ctx)
    
@bot.command(name='shuffle', help='shuffles discard into deck. Add `False` to leave discard pile as-is')
async def shuffle(ctx, add_discard=True):
    if add_discard== True:
        temp = discard_pile.deal(len(discard_pile))
        deck.add(temp)
        deck.shuffle()
    else:
        deck.shuffle()
    
@bot.command(name='deal', help='deals X cards to each player in game')
async def deal(ctx, num: int):
    for i in range(num):
        for player in players:
            temp=list(deck.deal(1))
            players[player][0] += temp
    await table(ctx)
    await hand(ctx)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)
