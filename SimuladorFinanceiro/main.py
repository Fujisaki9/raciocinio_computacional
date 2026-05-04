"""Inicia o simulador e gerencia o fluxo principal do programa."""

from rich import print as rprint
from simulators import JurosSimples, JurosCompostos
import view
import services

def main():
    view.mostrar_menu()
    opcao = services.validar_integer("[bold green]Escolha uma opção:[/] ")
    match opcao:
        case 1:
            aporte_inicial = services.validar_float("[bold yellow]Aporte inicial: R$[/]  ")
            taxa_juros = services.validar_float("[bold yellow]Taxa de juros mensal (%):[/]  ")
            tempo_investimento = services.validar_float("[bold yellow]Tempo de investimento (meses):[/]  ")
            taxa_inflacao = services.validar_float("[bold yellow]Inflação no período (%):[/]  ")
                
            # Cria o objeto Juros Simples
            juros_simples = JurosSimples(aporte_inicial, taxa_juros, tempo_investimento, taxa_inflacao)
    
            # Faz os cálculos e armazena-os dentro de um dicionário
            dicionario = juros_simples.coletar_dados_simulacao()
    
            # Mostra uma tabela com o resultado da simulação
            view.mostrar_relatorio_final(services.formatar_relatorio_final(dicionario))
    
            # Insere o resultado da simulação dentro de um arquivo.txt caso o usuário queira
            services.inserir_dados_txt(dicionario)
    
    
        case 2:
            aporte_inicial = services.validar_float("[bold yellow]Aporte inicial: R$[/]  ")
            taxa_juros = services.validar_float("[bold yellow]Taxa de juros mensal (%):[/]  ")
            tempo_investimento = services.validar_float("[bold yellow]Tempo de investimento (meses):[/]  ")
            aporte_mensal = services.validar_float("[bold yellow]Aporte mensal: R$[/]  ")
            taxa_inflacao = services.validar_float("[bold yellow]Inflação no período (%):[/]  ")
    
            # Cria o objeto Juros Compostos
            juros_compostos = JurosCompostos(aporte_inicial, taxa_juros, tempo_investimento, aporte_mensal, taxa_inflacao)
    
            # Faz os cálculos e armazena-os dentro de um dicionário
            dicionario = juros_compostos.coletar_dados_simulacao()
    
            # Mostra uma tabela com o resultado da simulação
            view.mostrar_relatorio_final(services.formatar_relatorio_final(dicionario))
    
            # Insere o resultado da simulação dentro de um arquivo.txt caso o usuário queira
            services.inserir_dados_txt(dicionario)
    
        case 3:
            rprint("[bold green]Programa encerrado![/]")


        case _:
            rprint("[bold red]ERRO: Algo deu errado![/]")
            

if __name__ = "__main__":
    main()
