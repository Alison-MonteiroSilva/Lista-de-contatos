import funções

# Lista que armazenas todos os contatos
lista_de_contatos = []

while True:
  # Legenda
  print("\nLista de Contatos 📱")

  print("1. Criar um novo contato")     # Create
  print("2. Listar todos os contatos")  # Read
  print("3. Listar apenas favoritos")
  print("4. Editar um contato")         # Update
  print("5. Deletar um contato")        # Delete
  print("6. Sair")

  escolha = input("\nEscolha uma das opções acima: ")

  if escolha == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número do contato: ")
    email = input("Digite o email do contato: ")
  
    # Função
    funções.criar_novo_contato(lista_de_contatos, nome, telefone,
    email)

  elif escolha == "2":
    funções.listar_contatos(lista_de_contatos)

  elif escolha == "3":
    funções.listar_favoritos(lista_de_contatos)

  elif escolha == "4":
      funções.listar_contatos
      funções.editar_contato(lista_de_contatos)

  elif escolha == "6":
    print("Programa encerrado 👋")
    break
