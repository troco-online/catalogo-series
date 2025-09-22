import json
import re

arquivo_json = "catalogo.json"
saida_json = "catalogo_sem_aspas.json"

# Ler JSON
with open(arquivo_json, "r", encoding="utf-8") as f:
    dados = json.load(f)

# Função para remover todas as aspas duplas
def remover_aspas(nome):
    # Remove todas as aspas duplas
    return nome.replace('""', '').strip()

# Atualizar todos os títulos
for item in dados:
    item['nome'] = remover_aspas(item['nome'])

# Salvar JSON atualizado
with open(saida_json, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print(f"Títulos atualizados! Verifique o arquivo '{saida_json}'.")
