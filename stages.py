import pyfiglet
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

font = ["bubble","colossal","computer","crawford","doom", "epic", "fuzzy", "gothic","katakana","linux","nancyj-underlined","speed","tombstone", ]

logo = pyfiglet.figlet_format("hangman", font=random.choice(font))

win = ''' 
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱┃┃╱╱╭╯╰╮╱╱╱╱╱╱╱╱╱┃┃
┃┃╱╰╋━━┳━╮╭━━┳━┳━┻╮╭╋╮╭┫┃╭━┻╮╭╋┳━━┳━╮╭━━┫┃
┃┃╱╭┫╭╮┃╭╮┫╭╮┃╭┫╭╮┃┃┃┃┃┃┃┃╭╮┃┃┣┫╭╮┃╭╮┫━━╋╯
┃╰━╯┃╰╯┃┃┃┃╰╯┃┃┃╭╮┃╰┫╰╯┃╰┫╭╮┃╰┫┃╰╯┃┃┃┣━━┣╮
╰━━━┻━━┻╯╰┻━╮┣╯╰╯╰┻━┻━━┻━┻╯╰┻━┻┻━━┻╯╰┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯
╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭┳╮
┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╭╯╰┫┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃
╰╮╰╯╭┻━┳╮╭╮╭━━┳╮╭┳━━┳━━┳━━┳━━┳━╯┃╰╮╭┫╰━┳━━╮╭╮╭╮╭┳━━┳━┳━╯┃┃
╱╰╮╭┫╭╮┃┃┃┃┃╭╮┃┃┃┃┃━┫━━┫━━┫┃━┫╭╮┃╱┃┃┃╭╮┃┃━┫┃╰╯╰╯┃╭╮┃╭┫╭╮┣╯
╱╱┃┃┃╰╯┃╰╯┃┃╰╯┃╰╯┃┃━╋━━┣━━┃┃━┫╰╯┃╱┃╰┫┃┃┃┃━┫╰╮╭╮╭┫╰╯┃┃┃╰╯┣╮
╱╱╰╯╰━━┻━━╯╰━╮┣━━┻━━┻━━┻━━┻━━┻━━╯╱╰━┻╯╰┻━━╯╱╰╯╰╯╰━━┻╯╰━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╰━━╯'''