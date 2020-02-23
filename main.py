print("--------------------------------")
print("----------CONTATOS--------------")
print("--------------------------------")

contatos = {}

comando = "continue"

while comando != "sair": 
  print("                     ")
  comando = input("Digite o comando: (novo, pes, sair):")

  if comando == "novo":
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

  if comando == "pes":
    print("comando pes selecionado")