"""TaskTracker — ponto de entrada da aplicação CLI (Fase 2 do Bootcamp II)."""

import sys
from pathlib import Path

# Garante que o pacote 'modules' seja importável mesmo rodando 'python src/main.py'
sys.path.insert(0, str(Path(__file__).resolve().parent))

from modules.tarefas import (
    carregar_tarefas,
    cadastrar_tarefa,
    visualizar_tarefas,
)
from modules.utils import limpar_tela, pausar


def exibir_menu() -> None:
    """Desenha o menu principal no terminal."""
    print("\n===== TaskTracker =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair")
    print("=======================")


def main() -> None:
    """Loop principal da aplicação."""
    tarefas = carregar_tarefas()

    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
            pausar()

        elif opcao == "2":
            visualizar_tarefas(tarefas)
            pausar()

        elif opcao == "3":
            print("\n👋 Até logo! Suas tarefas estão salvas em data/tarefas_db.json")
            break

        else:
            print("⚠️  Opção inválida. Tente novamente.")
            pausar()


if __name__ == "__main__":
    main()