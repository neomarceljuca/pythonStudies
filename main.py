from pokeapi import PokeAPI
import pprint


#setup

pokeapi = PokeAPI()



#interactive step

pesquisa1 = pokeapi.consulta("typhlosion")
pprint.pprint(pesquisa1)