import json
import requests
from CrossCutting.GcServiceConfiguration import GcServiceConfiguration
from domain.json.RootJson import Root

class GcService():
    def __init__(self, gcConfiguration: GcServiceConfiguration):
        self.__baseUrl = gcConfiguration.referer
        self.__lobbyUrl = gcConfiguration.referer + "lobby/match/{matchId}/1"
        self.__headers = {
            "authority": gcConfiguration.authority,
            "accept": gcConfiguration.accept,
            "user-agent": gcConfiguration.user_agent,
            "referer": gcConfiguration.referer,
            "cookie": gcConfiguration.cookie
        }

    def lista_ultimas_partidas(self):
        pass

    def detalhes_partida(self, matchId):
        url = self.__lobbyUrl.format(matchId=matchId)
        response = requests.get(url, headers=self.__headers)

        if response.status_code == 200:
            print("Request successful!")
            json_data = json.loads(response.text)
            root = Root(**json_data) 
            return root
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None