import os
from datetime import datetime

DATA_FORMATO = "%d/%m/%Y"

def limpar_tela() -> None:
    """Limpa o terminal (Windows: cls | Unix: clear)."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar(mensagem: str = "\nPressione ENTER para continuar...") -> None:
    """Aguarda o usuário pressionar ENTER."""
    input(mensagem)

def validar_titulo(titulo: str) -> bool:
    """True se o título não for vazio nem composto só por espaços."""
    return bool(titulo and titulo.strip())

def validar_data(data_str: str):
    """Valida o formato DD/MM/AAAA. Retorna datetime ou None."""
    try:
        return datetime.strptime(data_str.strip(), DATA_FORMATO)
    except (ValueError, AttributeError):
        return None

def normalizar_prioridade(prioridade: str):
    if not prioridade:
        return None
    mapa = {
        "alta":  "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }
    return mapa.get(prioridade.strip().lower())

def ler_titulo() -> str:
    """Solicita o título até que seja válido."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if validar_titulo(titulo):
            return titulo
        print("⚠️  Erro: o título não pode ficar em branco.")


def ler_data() -> str:
    while True:
        data_str = input("Data limite (DD/MM/AAAA): ").strip()
        if validar_data(data_str):
            return data_str.strip()
        print("⚠️  Erro: formato de data inválido. Use DD/MM/AAAA.")


def ler_prioridade() -> str:
    while True:
        prioridade = input("Prioridade (Alta/Média/Baixa): ").strip()
        normalizada = normalizar_prioridade(prioridade)
        if normalizada:
            return normalizada
        print("⚠️  Erro: prioridade inválida. Use Alta, Média ou Baixa.")