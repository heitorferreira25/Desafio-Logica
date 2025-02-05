# Nesse desafio e no três eu utilizei pesquisas para me auxiliar no desenvolvimento pois tive algumas dúvidas

def maior_letra_minuscula(texto: str) -> str:
    # Mostra só as letras minúsculas na string
    letras_minusculas = [letra for letra in texto if letra.islower()]
    # Traz a maior letra segundo a ordem alfabética ou uma mensagem informativa caso não tiver letras minúsculas
    return max(letras_minusculas) if letras_minusculas else "Sem letras minúsculas na string"


resultados = []
# O for para repetir as Strings de input
for i in range(1, 4):
    entrada = input(f"Digite a string {i}: ")
    resultado = maior_letra_minuscula(entrada)
    resultados.append(resultado)

# Para repetir as Strings de Output
for i, resultado in enumerate(resultados, start=1):
    print(f"Entrada {i}: Maior letra = '{resultado}'")
