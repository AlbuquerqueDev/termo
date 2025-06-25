import random


def main():
    lista_palavras = carregar_palavras("palavras/palavras_5_letras.txt")
    segredo = random.choice(list(lista_palavras))
    print(f"A palavra secreta é: {segredo}")
    print("-----\n")


def carregar_palavras(path: str):
    lista_palavras = set()
    with open(path, "r") as arquivo:
        for linha in arquivo.readlines():
            palavra = linha.strip().upper()
            lista_palavras.add(palavra)
    return lista_palavras


if __name__ == "__main__":
    main()
