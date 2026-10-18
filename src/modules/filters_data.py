from datetime import datetime, timedelta

from .utils import validar_data


def _parse_data(data_str: str):
    return validar_data(data_str)


def _fim_da_semana(hoje: datetime) -> datetime:
    return hoje + timedelta(days=7)


def _fim_do_mes(hoje: datetime) -> datetime:
    if hoje.month == 12:
        proximo = hoje.replace(year=hoje.year + 1, month=1, day=1)
    else:
        proximo = hoje.replace(month=hoje.month + 1, day=1)
    return proximo - timedelta(days=1)


def filtrar_tarefas(tarefas: list, periodo: str) -> list:
    if periodo == "todas":
        return list(tarefas)

    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    if periodo == "hoje":
        inicio, fim = hoje, hoje
    elif periodo == "semana":
        inicio, fim = hoje, _fim_da_semana(hoje)
    elif periodo == "mes":
        inicio = hoje.replace(day=1)
        fim = _fim_do_mes(hoje)
    else:
        return []

    resultado = []
    for tarefa in tarefas:
        data_tarefa = _parse_data(tarefa.get("data_limite", ""))
        if data_tarefa and inicio <= data_tarefa <= fim:
            resultado.append(tarefa)
    return resultado


def rotulo_periodo(periodo: str) -> str:
    return {
        "hoje":   "Hoje",
        "semana": "Próximos 7 dias",
        "mes":    "Este mês",
        "todas":  "Todas as tarefas",
    }.get(periodo, periodo)