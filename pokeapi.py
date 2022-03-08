import requests
import json

class PokeAPI:
#default constructor for lib implementation
    def __init__(self):
        return

#builds the relatory in a agreggation of lists and dictionaries.
#delivers the following format:
#[Name,[Types], [Abilities {name: description}], [Stats {name: value}], Official artwork link]
    def __relatorio1(self,dicionario):
        name = dicionario["name"].capitalize()

        foundTypes = dicionario["types"]
        types = ["*TYPES:"]
        for i in foundTypes:
            types.append(i["type"]["name"].capitalize())
        officialArt = ["*ARTWORK: ",dicionario["sprites"]["other"]["official-artwork"]["front_default"]]
        
        foundStats = dicionario["stats"]
        stats = ["*STATS:"]
        for j in range(0,len(foundStats)):
            stat = {foundStats[j]["stat"]["name"].capitalize(): foundStats[j]["base_stat"]}
            stats.append(stat)

        foundAbilities = dicionario["abilities"]  
        abilities  = ["*ABILITIES"] 
        for i in foundAbilities:
            desc = json.loads(requests.get(i["ability"]["url"]).text)["effect_entries"][1]["short_effect"]
            ability = {i["ability"]["name"]: desc}
            if i["is_hidden"]:
                ability[i["ability"]["name"] + " (HIDDEN)"] = ability[i["ability"]["name"]]
                del ability[i["ability"]["name"]] 
            abilities.append(ability)

        relatorio = [name,types,abilities,stats,officialArt]
        return relatorio

#retorns dictionary according to the search by pokemon name. Works with any capitalization
#prints error 404 in case a pokemon was not found.
    def consulta(self,nome):
        try:
            req = requests.get('https://pokeapi.co/api/v2/pokemon/' + str.lower(nome))
            dicionario = json.loads(req.text)
            return self.__relatorio1(dicionario)
        except:
            print("Erro na conexao " + str(req.status_code) + ": Pokemon " + nome + " nao encontrado.")
            return None



