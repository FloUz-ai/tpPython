# -*- coding: utf8 -*-

import random
import json

'''Lancer les scrapper characters et quote avant de lancer ce programme.
utiliser la commande :  scrapy runspider charactersScraper.py -o characters.json
Attention, fileQuotes et fileCharacters doivent correspondre au nom du fichier
creer avec cette commande'''

#Mettre les bons noms de clef et de fichier ci dessous

keyQuotes = "quote"
fileQuotes = "quotes.json"

keyCharacters = "character"
fileCharacters = "characters.json"

#initialisation de la valeur d'entrée utilisateur

userAnswer = " "

#Lecture fichier JSON

def readJson(file, key):
    list=[]
    with open(file) as f:
        readData = json.load(f)
        for item in readData:
            list.append(item[key])
    return list

#Choix d'un indice de liste au hasard

def randomQuotes (listX):
    quoteToPrint = random.randint(0, len(listX)-1)
    return quoteToPrint


#Creation des listes

listQuotes = readJson (fileQuotes, keyQuotes)
listCharacters = readJson (fileCharacters, keyCharacters)

#Main

while userAnswer != "B":
    print ("\n" ,"{} vous dit : {}".format(listCharacters[ randomQuotes(listCharacters)], listQuotes[ randomQuotes(listQuotes)]))
    userAnswer = input ("\nVeiller entrer une lettre. Preser \"B\" pour exit: ")
    
print ("\nMerci au revoir")



