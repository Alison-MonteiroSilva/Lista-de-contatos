import funções

# Lista que armazenas todos os contatos
lista_de_contatos = []

while True:
  # Legenda
  print("\n"+ "="* 40)
  print("📱         LISTA DE CONTATOS         📱")
  print("═" * 40)

  # Opções
  print(" [1] ➕ Criar novo contato")
  print(" [2] 📋 Listar todos os contatos")
  print(" [3] ⭐ Listar favoritos")
  print(" [4] ✏️ Editar contato")
  print(" [5] 🗑️ Deletar contato")
  print(" [0] 🚪 Sair")
  print("═" * 40)

  escolha = input("\nEscolha uma das opções acima: ")

  if escolha == "1":
    funções.criar_novo_contato(lista_de_contatos)

  elif escolha == "2":
    funções.listar_contatos(lista_de_contatos)

  elif escolha == "3":
    funções.listar_favoritos(lista_de_contatos)

  elif escolha == "4":
      funções.editar_contato(lista_de_contatos)

  elif escolha == "5":
    funções.excluir_contato(lista_de_contatos)

  elif escolha == "6":
    print("Programa encerrado 👋")
    break
