import os, json

# pasta onde estão as imagens
pasta_imagens = "imagens"

# lista de arquivos
arquivos = os.listdir(pasta_imagens)

catalogo = []

for arquivo in arquivos:
    if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
        nome = os.path.splitext(arquivo)[0]  # tira extensão
        # transforma o nome do arquivo em título bonitinho
        nome_formatado = nome.replace("-", " ").replace("_", " ").title()

        catalogo.append({
            "nome": nome_formatado,
            "imagem": f"{pasta_imagens}/{arquivo}",
            "preco": "R$ 10,00"
        })

# salva em catalogo.json
with open("catalogo.json", "w", encoding="utf-8") as f:
    json.dump(catalogo, f, ensure_ascii=False, indent=2)

print(f"✅ Catálogo gerado com {len(catalogo)} itens em catalogo.json")
