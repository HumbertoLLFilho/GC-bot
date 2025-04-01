import json, os
from ExternalServices.GCService import GcService
from domain.Campeonato import Campeonato
from domain.json.RootJson import Root
from CrossCutting.GcServiceConfiguration import GcServiceConfiguration
from domain.partida import Partida
import pandas as pd

keys_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys.json")

with open(keys_file, 'r', encoding='utf-8') as f:
    keys_data = json.load(f)
    gc_config = GcServiceConfiguration(**keys_data["GcServiceConfiguration"])

gcService = GcService(gc_config)

partidas = [
    23334827,
    23334727,
    23334444,
    23334133,
    23333620,
    23332956,
    23331984
]

campeonato = Campeonato()
for partidaId in partidas:
    root = gcService.detalhes_partida(partidaId)

    partida = Partida().from_json(root)
    campeonato.adiciona_partida(partida)
    data = []

for partida in campeonato.partidas:
  for time in partida.times:
    for jogador in time.jogadores:
      data.append({
        "Mapa": partida.mapa,
        "Hora": partida.data,
        "Resultado": partida.resultado,
        "Time": time.nome,
        "Jogador": jogador.nome,
        "Kills": int(jogador.kills),
        "Mortes": int(jogador.mortes),
        "Assistências": int(jogador.assistencias),
        "adr": float(jogador.adr),
        "kd": float(jogador.kd),
      })

df = pd.DataFrame(data)
output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "partidas.xlsx")
df.to_excel(output_file, index=False)

print(f"Excel file saved to {output_file}")