import character_films
import json

listofchar=[]

def llegir_json(file):
    with open(file, "r", encoding="utf-8") as char:
        starwars = json.load(char)