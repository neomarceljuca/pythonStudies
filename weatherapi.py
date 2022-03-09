import requests
import json
from datetime import datetime

class weatherAPI:
#default constructor for lib implementation
    def __init__(self, apiKey):
        self.key = apiKey
        return


    def requisicao(self, cityName):
        

        requisicao = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ cityName + "&appid=" + self.key).text)

        if requisicao["cod"] == 200:
            relatorio = {"API Report" : ""}
            relatorio["Date and time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            relatorio["City"] = requisicao["name"]
            relatorio["Country"] = requisicao["sys"]["country"]
            relatorio["Temperature"] = str(round(requisicao["main"]["temp"] - 273.15, 2)) + "C"
            relatorio["Weather"] = requisicao["weather"][0]["description"]
            relatorio["Humidity"] = str(requisicao["main"]["humidity"]) + "%"
            return relatorio
        else:
            return "Code" + requisicao["cod"] + ": Research failed."