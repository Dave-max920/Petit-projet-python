import json

with open("SE_devoir.json", "r", encoding="utf-8") as file:
    fichier=json.load(file)
    
with open("SE_devoir.json", "r", encoding="utf-8") as file:
    json.dump(fichier, file, indent=4)

