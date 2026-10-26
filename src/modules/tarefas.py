import json
from datetime import datetime
from pathlib import Path

from .filtros_data import filtrar_tarefas, rotulo_periodo
from .utils import limpar_tela, ler_titulo, ler_data, ler_prioridade, validar_data

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "data" / "tarefas_db.json"

def carregar_tarefas() -> list:
    """Lê o JSON local. Retorna [] se não existir ou estiver corrompido."""
    if not DB_PATH.exists():
        return []
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def salvar_tarefas(tarefas: list) -> None:
    """Grava a lista no JSON (cria a pasta se necessário)."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def cadastrar_tarefa(tarefas: list) -> list:
    """Executa o fluxo completo de cadastro (Passo a Passo da Fase 1)."""
    print("\n--- Nova Tarefa ---")
    titulo      = ler_titulo()
    data_limite = ler_data()
    prioridade  = ler_prioridade()
    descricao   = input("Descrição (opcional): ").strip()

    tarefa = {
        "titulo":      titulo,
        "descricao":   descricao,
        "prioridade":  prioridade,
        "data_limite": data_limite,
        "status":      "Pendente",
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("\n✅ Tarefa cadastrada com sucesso!")
    return tarefas

def exibir_tarefas(tarefas: list) -> None:
    """Imprime as tarefas formatadas ou mensagem de lista vazia."""
    if not tarefas:
        print("\n📭 Você não tem nenhuma tarefa cadastrada para este período.")
        return

    print()
    total_tarefas = len(tarefas)
    for i, t in enumerate(tarefas, start=1):
        numero = total_tarefas - i + 1
        status = "✅" if t["status"] == "Concluída" else "🕒"
        print(f"[{numero}] {status} {t['titulo']}")
        print(f"     Descrição : {t.get('descricao') or '(sem descrição)'}")
        print(f"     Data      : {t['data_limite']}")
        print(f"     Prioridade: {t['prioridade']}")
        print(f"     Status    : {t['status']}")
        print()


def visualizar_tarefas(tarefas: list) -> None:
    """Executa o fluxo de visualização com filtros temporais."""
    print("\n--- Visualizar Tarefas ---")
    print("1 - Hoje")
    print("2 - Próximos 7 dias")
    print("3 - Este mês")
    print("4 - Todas")

    opcao = input("\nEscolha o filtro: ").strip()
    limpar_tela()
    mapa = {"1": "hoje", "2": "semana", "3": "mes", "4": "todas"}
    periodo = mapa.get(opcao)

    if not periodo:
        print("⚠️  Opção inválida.")
        return

    while True:
        filtradas = sorted(
            filtrar_tarefas(tarefas, periodo),
            key=lambda tarefa: validar_data(tarefa.get("data_limite", "")) or datetime.max,
            reverse=True,
        )
        print(f"\n=== {rotulo_periodo(periodo)} ===")
        exibir_tarefas(filtradas)

        if not filtradas:
            return

        escolha = input(
            "\nDigite o número da tarefa para marcá-la como concluída (0 para voltar): "
        ).strip()
        if escolha == "0":
            return

        try:
            numero = int(escolha)
        except ValueError:
            print("⚠️  Número inválido.")
            continue

        if not 1 <= numero <= len(filtradas):
            print("⚠️  Número de tarefa inválido.")
            continue

        tarefa_selecionada = filtradas[len(filtradas) - numero]
        indice = next(
            i for i, tarefa in enumerate(tarefas) if tarefa is tarefa_selecionada
        )
        marcar_concluida(tarefas, indice)
        limpar_tela()


def marcar_concluida(tarefas: list, indice: int) -> list:
    """
    Marca uma tarefa como 'Concluída' — só se estiver 'Pendente'.
    Regra da Fase 1: uma tarefa só pode ser concluída se estiver pendente.
    """
    if not (0 <= indice < len(tarefas)):
        print("⚠️  Índice inválido.")
        return tarefas

    tarefa = tarefas[indice]
    if tarefa["status"] == "Concluída":
        print("⚠️  Esta tarefa já está concluída.")
        return tarefas

    tarefa["status"] = "Concluída"
    salvar_tarefas(tarefas)
    print("✅ Tarefa marcada como concluída!")
    return tarefas