login = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if (login == "admin") and (senha == "123"):
    print("Olá admin, seja bem-vindo!")
else:
    print("Login ou senha incorretos, tente novamente")