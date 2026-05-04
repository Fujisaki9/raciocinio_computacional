""" Contém funções utilitárias para formatação visual e estilização do terminal. """

from rich import print as rprint
from rich.console import Console
from rich.rule import Rule


def linha():
    console = Console()
    console.print(Rule(characters = "-", style = "white"))


def imprimir_negrito(texto: str) -> str:
    console = Console()
    return console.input(f"[bold]{texto}[/]")


def formatar_amarelo_negrito(texto: str) -> str:
    console = Console()
    return console.input(f"[bold yellow]{texto}[/]")


def imprimir_italico(texto: str):
    rprint(f"[i bold]{texto}[/]")


def imprimir_italico_vermelho(texto: str):
    rprint(f"[i bold red]{texto}[/]")


def formatar_italico(texto: str, end = ' ') -> str:
    console = Console()
    return console.print(f"[i bold]{texto}[/]", end = end)
