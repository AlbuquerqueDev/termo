def filtrar_palavras(caminho, tamanho):
    palavras_5_letras = []
    try:
        with open(caminho, "r", encoding="utf-8") as a:
            for linha in a:
                word = linha.strip()
                if len(word) == tamanho and word.isalpha():
                    palavras_5_letras.append(word)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
    return palavras_5_letras


nome_arquivo = "palavras.txt"
palavras_5_letras = filtrar_palavras(nome_arquivo, 5)

print(f"Foram encontradas {len(palavras_5_letras)} palavras de 5 letras.")

with open("palavras_5_letras.txt", "w", encoding="utf-8") as a:
    for palavra in palavras_5_letras:
        a.write(palavra + "\n")
print("As palavras de 5 letras foram salvas em 'palavras_5_letras.txt'")
