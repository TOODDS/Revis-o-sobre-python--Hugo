nome = input("Digite o seu nome: ")
dis = input("Qual é o nome da disciplina: ")
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida, tente novamente!")
else:
    if 5.5 <= nota < 6:
        nota = 6.0
    if nota >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    print(f'{nome}, você está {situacao} na disciplina de {dis} com a nota {nota}')
