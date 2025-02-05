def formatar_nome(nome_completo: str) -> str:
    # Esse método divide o nome em parte
    nomes = nome_completo.strip().split()

    # Verifica se tem no minimo dois nomes
    if len(nomes) < 2:
        return "Nome inválido. Digite pelo menos um nome e um sobrenome."

    # Último sobrenome em letra maiúscula
    ultimo_sobrenome = nomes[-1].upper()

    # As iniciais dos outros nomes serão em maiúsculas
    iniciais = [nome[0].upper() for nome in nomes[:-1]]

    # Formata o resultado
    resultado = f"{ultimo_sobrenome}, " + ". ".join(iniciais) + "."

    return resultado

    # Retorna o resultado
def formatacao_dos_nomes():
    for i in range(1, 4):
        nome = input(f"Digite o nome completo {i}: ")
        print("Formato:", formatar_nome(nome))


formatacao_dos_nomes()