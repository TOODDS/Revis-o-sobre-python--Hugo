def adi(x, y):
    return x + y
def sub(x, y):
    return x - y
def divi(x, y):
    if y == 0:
        return("Erro! divisão por zero!")
    else:
        return x / y
def multi(x, y):
    return x * y
def pote(x):
    return x * x

rep = True  

while 1:  
    print('''Olá, você deseja acessar a calculadora?
1- Sim
2- Não''')
    op = input(": ")
    
    if op == "1":
        while rep: 
            escolha = input('''     ----- Cal.py -----
1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- Elevar ao quadrado
0- Sair
Escolha uma operação: ''')
            if escolha == "1":
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f'{num1} + {num2} =', adi(num1, num2))
            elif escolha == "2":
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f'{num1} - {num2} =', sub(num1, num2))
            elif escolha == "3":
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f'{num1} * {num2} =', multi(num1, num2))
            elif escolha == "4":
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f'{num1} / {num2} =', divi(num1, num2))
            elif escolha == "5":
                num1 = int(input("Digite o número que você quer elevar ao quadrado: "))
                print(f'{num1} ^ 2 =', pote(num1))
            elif escolha == "0":
                rep = False
            else:
                print("Informação dada errada! Tente novamente!")
    elif op == "2":
        print("Puxa que pena :(")
        break  
    else:
        print("Informação dada errada! Tente novamente: ")
