from discord.ext import commands
import discord
import random
import datetime
import sqlite3

def setup(client):
    client.add_cog(prefix(client))
