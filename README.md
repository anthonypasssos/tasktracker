# TaskTracker

Aplicativo de linha de comando para cadastrar, consultar e concluir tarefas. Os dados são salvos localmente em `data/tarefas_db.json`.

## Guia de Execução com Docker

Para rodar a aplicação no seu ambiente, certifique-se de ter o Docker e o Docker Compose instalados. Execute os comandos exatos abaixo:

### 1. Construir a imagem (Build)
```bash
docker build -t tasktracker-app .

## Requisitos

- Python 3.9 ou superior
- Terminal ou prompt de comando

O projeto usa apenas a biblioteca padrão do Python, então não é necessário instalar dependências.

## Como executar

Na pasta raiz do projeto, execute:

```bash
python3 src/main.py
```

No Windows, se o comando `python3` não estiver disponível, use:

```powershell
python src/main.py
```

## Como usar

O menu principal oferece estas opções:

1. **Cadastrar nova tarefa** — informe um título, uma data limite no formato `DD/MM/AAAA` e uma prioridade (`Alta`, `Média` ou `Baixa`). A descrição é opcional.
2. **Visualizar tarefas cadastradas** — escolha um filtro:
   - **Hoje**: tarefas com prazo para hoje.
   - **Próximos 7 dias**: tarefas com prazo entre hoje e os próximos sete dias.
   - **Este mês**: tarefas com prazo no mês atual.
   - **Todas**: todas as tarefas cadastradas.

   As tarefas são exibidas da data limite mais distante à mais próxima. O número `[1]` identifica a tarefa com o prazo mais próximo. Para marcar uma tarefa como concluída, digite o número dela; a lista será atualizada e continuará aberta. Digite `0` para voltar ao menu.
3. **Sair** — encerra o aplicativo.

Ao cadastrar ou concluir uma tarefa, as alterações são salvas automaticamente em `data/tarefas_db.json`. Esse arquivo é criado quando necessário.
