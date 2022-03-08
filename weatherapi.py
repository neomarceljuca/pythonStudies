import requests
import json

class weatherAPI:
#default constructor for lib implementation
    def __init__(self, apiKey):
        self.key = apiKey
        return


    def requisicao(self):
        requisicao = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q=fortaleza" + "&appid=" + self.key).text)
        return requisicao