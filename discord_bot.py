import discord
from discord import channel
import requests
import json
import random
import giphy_client
from requests import api
import stages
import pyfiglet
from word_list import words
import string
import os
from os.path import join, dirname
from dotenv import load_dotenv
from giphy_client.rest import ApiException

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def get_advice():
  response = requests.get('https://api.adviceslip.com/advice')
  json_data = json.loads(response.text)
  advice = json_data['slip']['advice']
  return advice



def get_gify(q):

  gify_api_key = os.environ.get("GIPHY_API")
  api_instance = giphy_client.DefaultApi()

  try:
    api_response = api_instance.gifs_search_get(gify_api_key,q,limit=5,rating = "r")
    lst = list(api_response.data)
    giff = random.choice(lst)
    return giff.embed_url

  except ApiException as e:
    print(e)

def get_tenor(query):
  tenor_api_key = os.environ.get("TENOR_KEY")
  limit = 8

  r = requests.get(f"https://g.tenor.com/v1/search?q={query}&key={tenor_api_key}&limit={limit}")

  if r.status_code == 200:
      
      top_8gifs = json.loads(r.content)
      random_gif = random.randint(0,5)

      return top_8gifs["results"][random_gif]["media"][0]["gif"]["url"]
  

def get_insults():
  response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
  json_data = json.loads(response.text)
  insult =  json_data['insult']
  return insult
  
def get_bill(name):
  sex = ["m","f"]
  url = "https://belikebill.ga/billgen-API.php?default=1&name=" + name + "&sex=" + random.choice(sex)
  return url


def help():
  commands = '''
>gif [type_0f_gif] : to request a gif from Tenor 
>gify [type_0f_gif] : to request a gif from Gify
>insults : get any kind of insult 
>advice : get any childish advices
>belike [anyone] : to get a BeLikeBill meme auto generated which will replace `Bill` with `anyone`
>play : to play the game Hangman
'''
  return commands


client = discord.Client()

lost = ["sad", "agonizing", "hurtful","pain", "painful", "cry", "crying", "sobing"]
win = ["celeberation", "party", "cheers", "happiness", "Good job", "proud"]


@client.event
async def on_ready():
  print('We have logged in as {0.user} '.format(client))


@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('>insult'):
    insult = get_insults()
    await message.channel.send(insult)
  
  if message.content.startswith('>advice'):
    advice = get_advice()
    await message.channel.send(advice)

  if message.content.startswith('>belike'):
     name = message.content.split(">belike ",1)[1]
     await message.channel.send(get_bill(name))

  if message.content.startswith('>gify'):
   q = message.content.split(">gify ",1)[1]
   await message.channel.send(get_gify(q))
  
  if message.content.startswith('>gif'):
   q = message.content.split(">gif ",1)[1]
   await message.channel.send(get_tenor(q))   
  
  if message.content.startswith('>help'):
    await message.channel.send(help())
  

  if message.content.startswith('>play'):
    
    result = "```"+pyfiglet.figlet_format("hangman", font=random.choice(stages.font))+"```\n"
    await message.channel.send(result)
    end_of_game = False

    answer = list(words[random.randint(0,len(words)-1)])
    # await message.channel.send(answer)
    
    
    no_of_blanks = []
    total_lives = 6
    total_guess = []

    for letter in answer:
        no_of_blanks += '-'


    await message.channel.send("```"+str(no_of_blanks)+"```")
    await message.channel.send("Guess the word:\n")
  
    while not end_of_game:
      
        count = 0
        wrong_count = 0
        
        def check(m):
            if m.content in alphabet_list and m.channel == message.channel:
                return m
            elif m.content == ">stop":
              quit = True
              return quit
        
       
        guess = await client.wait_for("message", check=check)
        if guess.content == ">stop":
          await message.channel.send("Quiting..")
          break
      
                                                                     
        for letter in answer:
            count += 1
            if guess.content in total_guess:
                await message.channel.send("You have already guessed that letter")
                break
            elif(guess.content == letter):
                
                no_of_blanks[count-1] = guess.content
            else:
                
                wrong_count+=1
                
        if(wrong_count == len(answer)):
            
            await message.channel.send("```"+stages.stages[total_lives]+"```")
            await message.channel.send(f"wrong guess, you lose a life! {total_lives} lives remaining\n")
            total_lives -=1
            
            if total_lives == -1:
                await message.channel.send(get_gify(lost[random.randint(0,len(lost)-1)]))
                await message.channel.send(f"{message.author} , you've lost 😪")
                await message.channel.send(f"The word was {''.join(answer)} \n")
                end_of_game = True
                break    
        # await message.channel.send(wrong_count)    
        # await message.channel.send(count)
        total_guess.append((guess.content))        
        await message.channel.send("```"+str(no_of_blanks)+"```")
        await message.channel.send("As of now, you have guessed :-```" +str(total_guess) + "``` \n")
        if "-" not in no_of_blanks:
            await message.channel.send("```"+stages.win+"```")
            await message.channel.send(get_gify(win[random.randint(0,len(win)-1)]))
            await message.channel.send(f"{message.author} took {len(total_guess)} tries to guess the word")
            end_of_game = True
    
    
client.run(os.environ.get("BOT"))