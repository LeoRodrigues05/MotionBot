import discord as ds
import os
import json
import random
from replit import db
import requests
from THWmotions.py import THW



client = ds.Client()

command_list = ["$Hello - gesture", "$Bye - gesture", "$MatchupAP - creates a matchup based on team1 and team2", "$Coinflip - essential tool for deciding motions!", "$MatchupBP - creates a matchup for a BP based on team numbers (i.e. 1,2,3,4)"]

thw_motions = ["THW introduce Mandatory Organ Donation", "THW abolish trial by jury", "THW remove all non-military sanctions on Iran"] + THW


def get_helps():
  text = " "
  for i in range(len(command_list)):
    text = text + command_list[i] + '\n'  
  text = text + "\n These are the basic functions one can use on this bot. Many more to come!"
  return (text)  

@client.event
async def on_ready():
  print("This bot is online now as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$Hello"):
    await message.channel.send("Welcome to the Motion Generating Bot!")
  
  if message.content.startswith("$Bye"):
    await message.channel.send("Goodbye!")
  
  if message.content.startswith("$MatchupAP"):
    x = random.randint(0,1)
    temp = ['Government', 'Opposition']
    if x==1:
      final = "Team1: " + temp[x] + "\nTeam2: " + temp[x-1]
    else:
      final = "Team1: " + temp [x] + "\nTeam2: " + temp[x+1]
    await message.channel.send(final) 

  if message.content.startswith("$coinflip"):
    x = random.randint(0,1)
    temp = ["Heads!", "Tails!"]
    await message.channel.send(temp[x])

  if message.content.startswith("$help"):
    text = get_helps()
    await message.channel.send(text)
  
  if message.content.startswith("$MatchupBP"):
    temp = ["1", "2", "3", "4"]
    random.shuffle(temp)
    final = "OG: "+temp[0]+"\nOO: "+temp[1]+"\nCG: "+temp[2]+"\nCO: " + temp[3]
    await message.channel.send(final)

  if message.content.startswith("$getTHW"):
    await message.channel.send("Your motion: " + random.choice(thw_motions))

  
     

client.run(TOKEN_BOT)
