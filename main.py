from pokeapi import PokeAPI
from weatherapi import weatherAPI
import pprint
import os

#setup

#helper methods
def clearScreen():
    clear = lambda: os.system('cls')
    clear()
    return


#interactive section
opt = ""
while opt != 0:
    print("API Interaction Test via Python --- Main Menu \nBy Marcel Juca")
    opt = input("Type Option and hit ENTER:\n1)OpenWeather\n2)PokeAPI\n0)Exit\n")
    
    if opt == "1":
    #Open Weather
        mykey = input("Open Weather-\nInsert OpenWeather APIKey:\n")
        weatherapi = weatherAPI(mykey)

        exit = False
        while not exit:
            op = input("Input a city name or EXIT to leave to main menu.")
            if str.upper(op) == "EXIT":
                exit = True
                clearScreen()
                continue
            else:
                pesquisa1 = weatherapi.requisicao(op)
                if pesquisa1 is None:
                    continue
            pprint.pprint(pesquisa1)



    elif opt == "2":
    #PokeAPI
        pokeapi = PokeAPI()   
        exit = False
        while not exit:
            op = input("Input a pokemon name or EXIT to leave to main menu.")
            if str.upper(op) == "EXIT":
                exit = True
                clearScreen()
                continue
            else:
                pesquisa1 = pokeapi.consulta(str.lower(op))
                if pesquisa1 is None:
                    continue
            pprint.pprint(pesquisa1)
    elif opt == "0":
        break
    else:
        clearScreen()
        print("Opcao Invalida. Tente Novamente.")

