"""Interface visual do simulador (menus e tabelas)."""

from rich.console import Console
from rich.table import Table
from services import montar_tabela

def mostrar_menu():
    """
    Exibe o menu principal do simulador financeiro no console.
    """
    table = Table(header_style = "bold",
                  width = 24,
                  style = "blue")
    table.add_column("Simulador Financeiro", justify = "left")
    table.add_row("[bold][1] Juros Simples[/]")
    table.add_row("[bold][2] Juros Compostos[/]")
    table.add_row("[bold][3] Sair do programa[/]")
    console = Console()
    console.print(table)


def mostrar_relatorio_final(dicionario: dict):
    """
    Formata e exibe no console uma tabela detalhada com os resultados da simulação.
    Utiliza a biblioteca "rich".
    :param dicionario: Dicionário contendo os dados coletados da simulação.
    """
    print()
    table = Table(title = "[bold blue]Relatório Final - Simulação[/]",
                  style = "red")

    table.add_column("Descrição", style = "dim", width = 35)
    table.add_column("Valor", justify = "right")
    table.add_section()
    
    for i in montar_tabela():
        if i is None:
            table.add_section()
        else:
            descricao, chave = i
            table.add_row(f"[bold bright_white]{descricao}[/]", dicionario[chave])
            
    console = Console()
    console.print(table)


