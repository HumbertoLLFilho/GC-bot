import json, os

from domain.json.RootJson import Root

# Pega o json do jogo (feito)
# Formata o json (feito)
# passa todos os jogos (feito)
# pega os detalhes dos jogos
# Faz os calculos de partidas
# Salva o excel

diretorio = "C:\Users\hleit\Desktop\Pessoal\Dev\Estudos\GC bot\Games"

arquivos = os.listdir(diretorio)

for arquivo in arquivos:
  caminho_completo = os.path.join(diretorio, arquivo)
  
  if os.path.isfile(caminho_completo):
    if arquivo.endswith(".json"):
      caminho_arquivo = os.path.join(diretorio, arquivo)

      with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        root = Root.model_validate_json(f)


