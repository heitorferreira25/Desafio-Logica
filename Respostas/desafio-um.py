def calcular_media_dos_alunos():
    
    resultados = []
    # Solicita o nome do aluno
    for j in range(1, 4):
        print(f"\nAluno {j}:")
        nome = input("Digite o nome do aluno: ")

        soma_das_notas = 0
    # Solicita as notas das quatro provas
        for i in range(1, 5):
            while True:
                try:
                    nota = int(input(f"Digite a nota da prova {i}: "))
                    if 0 <= nota <= 10:
                        break
                    else:
                        print("A nota deve ser um número inteiro e de 0 a 10.")
                except ValueError:
                    print("Entrada inválida. Digite apenas números inteiros.")

            soma_das_notas += nota
    # Calcula a média aritmética 
        media = soma_das_notas / 4
        resultados.append((nome, media))
    # Retorna o resultado
    print("\nResultados:")
    for nome, media in resultados:
        print(f"Aluno = {nome}: Média = {media:.2f}")


calcular_media_dos_alunos()