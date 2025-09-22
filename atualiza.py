import json
import os

# Caminho do JSON e da pasta de imagens
json_path = "catalogo.json"
imagens_folder = "imagens"

# Carrega o JSON
with open(json_path, "r", encoding="utf-8") as f:
    dados = json.load(f)

# Atualiza cada item
for item in dados:
    # Extrai apenas o nome base do arquivo
    nome_antigo = os.path.basename(item["imagem"])
    
    # Lista todos os arquivos da pasta imagens
    arquivos = os.listdir(imagens_folder)
    
    # Procura arquivo que corresponda ao nome base (ignora extensão errada se houver)
    for arquivo in arquivos:
        if nome_antigo.split(".")[0] in arquivo:
            # Atualiza o campo imagem para o nome correto da pasta
            item["imagem"] = os.path.join(imagens_folder, arquivo)
            break

# Salva o JSON atualizado
with open("dados_atualizado.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

print("✅ JSON atualizado com sucesso!")
