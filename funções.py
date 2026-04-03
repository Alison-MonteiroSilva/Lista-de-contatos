# Criar um novo contato
def criar_novo_contato(lista_de_contatos, nome, telefone, email):
  contato = {"nome": nome, "telefone": telefone, "email": email}
  
  lista_de_contatos.append(contato)

  print(f"O contato 👤 {nome}, foi adicionado com sucesso! ✅")

  return

# Listar contatos
def listar_contatos(lista_de_contatos):
    if not lista_de_contatos:
        print("Lista de contatos vazia 📭")
        return

    contatos_ordenados = sorted(
        lista_de_contatos,
        key=lambda contato: contato["nome"].title()
    )

    while True:
        print("\n=== LISTA DE CONTATOS ===")
        for indice, contato in enumerate(contatos_ordenados, start=1):
            print(f"{indice}. {contato['nome']}")

        print("0. Voltar")

        escolha = input("\nSelecione o número do contato para visualizar: ").strip()

        if not escolha.isdigit():
            print("Digite apenas números.")
            continue

        escolha = int(escolha)

        if escolha == 0:
            print("Voltando...")
            break

        if escolha < 1 or escolha > len(contatos_ordenados):
            print("Contato inválido.")
            continue

        contato = contatos_ordenados[escolha - 1]

        while True:
            print("\n=== DETALHES DO CONTATO ===")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"E-mail: {contato['email']}")

            print("\n1. Voltar para a lista")
            print("0. Sair da visualização")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                break
            elif opcao == "0":
                return
            else:
                print("Opção inválida.")

# Editar contato existente
def editar_contato(lista_de_contatos):
    if not lista_de_contatos:
        print("Lista de contatos vazia 📭")
        return

    print("\n=== EDITAR CONTATO ===")

    for indice, contato in enumerate(lista_de_contatos, start=1):
        print(f"{indice}. {contato['nome']}")
        print(f"   Telefone: {contato['telefone']}")
        print(f"   E-mail: {contato['email']}")

    indice_selecionado = input("\nDigite o número do contato que deseja editar: ").strip()

    if not indice_selecionado.isdigit():
        print("Índice inválido. Digite apenas números.")
        return

    indice_selecionado = int(indice_selecionado) - 1

    if indice_selecionado < 0 or indice_selecionado >= len(lista_de_contatos):
        print("Contato não encontrado.")
        return

    contato = lista_de_contatos[indice_selecionado]

    print(f"\nContato selecionado: {contato['nome']}")
    print("O que deseja editar?")
    print("1. Nome")
    print("2. Telefone")
    print("3. E-mail")
    print("4. Todos")

    opcao = input("Escolha uma opção: ").strip()

    novo_nome = contato["nome"]
    novo_telefone = contato["telefone"]
    novo_email = contato["email"]

    if opcao == "1":
        novo_nome = input("Digite o novo nome: ").strip()

    elif opcao == "2":
        novo_telefone = input("Digite o novo telefone: ").strip()

    elif opcao == "3":
        novo_email = input("Digite o novo e-mail: ").strip()

    elif opcao == "4":
        novo_nome = input("Digite o novo nome: ").strip()
        novo_telefone = input("Digite o novo telefone: ").strip()
        novo_email = input("Digite o novo e-mail: ").strip()

    else:
        print("Opção inválida.")
        return

    print("\n=== CONFIRMAÇÃO DE EDIÇÃO ===")
    print(f"Nome atual: {contato['nome']} -> Novo nome: {novo_nome}")
    print(f"Telefone atual: {contato['telefone']} -> Novo telefone: {novo_telefone}")
    print(f"E-mail atual: {contato['email']} -> Novo e-mail: {novo_email}")

    confirmar = input("\nDeseja salvar as alterações? (s/n): ").strip().lower()

    if confirmar != "s":
        print("Edição cancelada.")
        return

    contato["nome"] = novo_nome
    contato["telefone"] = novo_telefone
    contato["email"] = novo_email

    print("Contato atualizado com sucesso ✅")