import funções
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

lista_de_contatos = []

while True:
    print("\n" + "=" * 40)
    print("📱         LISTA DE CONTATOS         📱")
    print("═" * 40)

    print(" [1] ➕ Criar novo contato")
    print(" [2] 📋 Listar todos os contatos")
    print(" [3] ⭐ Listar favoritos")
    print(" [4] ✏️  Editar contato")
    print(" [5] 🗑️  Deletar contato")
    print(" [6] 🚪 Sair")
    print("═" * 40)

    escolha = input("\nEscolha uma das opções acima: ").strip()

    if escolha not in ["1", "2", "3", "4", "5", "6"]:
        print("❌ Opção inválida! Escolha um número de 1 a 6.")
        input("\nPressione Enter para continuar...")
        continue

    if escolha == "1":
        funções.criar_novo_contato(lista_de_contatos)
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

    elif escolha == "2":
        funções.listar_contatos(lista_de_contatos)
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

    elif escolha == "3":
        funções.listar_favoritos(lista_de_contatos)
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

    elif escolha == "4":
        funções.editar_contato(lista_de_contatos)
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

    elif escolha == "5":
        funções.excluir_contato(lista_de_contatos)
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

    elif escolha == "6":
        limpar_tela()
        print("Programa encerrado 👋")
        break