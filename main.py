"""
Arquivo Principal - Gestor de Mangás.

Este arquivo é o ponto de entrada do programa.
Ele gerencia o menu e coordena as chamadas entre o visual (utils.py)
e a lógica de dados (services.py).
"""

from datetime import date
import utils
import services


def main():
    mangas_cadastrados = services.verificar_arquivo_json()
    while True:
        comando = utils.formatar_amarelo_negrito("Digite um comando: ").strip().upper()
        utils.linha()
        match comando:

            # Exibe informações sobre o autor e o projeto
            case "ABOUT":
                services.informacoes_autor_projeto()

            # Finaliza a execução do loop principal e encerra o programa
            case "QUIT":
                services.inserir_dados_json(mangas_cadastrados)
                services.encerrar_programa()
                break

            # Inicia o cadastro de novos mangás
            case "ADD":
                while True:
                    try:
                        quantidade = int(utils.imprimir_negrito("Quantos mangás deseja cadastrar? "))
                        utils.linha()
                        if quantidade <= 0:
                            utils.imprimir_italico_vermelho("Insira um valor válido, tente novamente!")
                        else:
                            services.cadastrar_novos_mangas(quantidade, mangas_cadastrados)
                            break
                    except ValueError:
                        utils.imprimir_italico_vermelho("Comando inválido, tente novamente!")

            # Mostra os dicionários armazenados dentro da lista de maneira ordenada
            case "LIST":
                services.listar_projetos_cadastrados(mangas_cadastrados)

            # Modifica as informações de um dicionário na lista
            case "UPDATE":
                nome_manga_alterar = utils.imprimir_negrito("Qual mangá deseja modificar?: ").strip().title()
                utils.linha()
                manga_alterar = services.procurar_manga_na_lista(nome_manga_alterar, mangas_cadastrados)
                if manga_alterar is not None:
                    manga_novo = utils.imprimir_negrito("Novo mangá: ").strip().title()
                    verificar_dados = services.verificar_manga_duplicado(manga_novo, mangas_cadastrados)
                    if verificar_dados:
                        utils.formatar_italico(f"O mangá {manga_novo} já está cadastrado\n")
                    else:
                        manga_alterar["nome"] = manga_novo
                        manga_alterar["concluido"] = services.validar_conclusao_obra()
                        data = date.today()
                        dados_atualizacao = (manga_alterar["nome"], manga_alterar["concluido"], data.strftime("%Y/%m/%d"))
                        manga_alterar["historico"].append(dados_atualizacao)
                        utils.imprimir_italico("Informações alteradas com sucesso!")
                    utils.linha()
                else:
                    utils.imprimir_italico("Esse mangá não foi cadastrado!")
                    utils.linha()

            # Remove um mangá da lista
            case "DELETE":
                nome_manga_deletar = utils.imprimir_negrito("Qual mangá deseja deletar?: ").strip().title()
                utils.linha()
                manga_deletar = services.procurar_manga_na_lista(nome_manga_deletar, mangas_cadastrados)
                if manga_deletar is not None:
                    mangas_cadastrados.remove(manga_deletar)
                    utils.formatar_italico(f"O mangá {manga_deletar['nome']} foi deletado com sucesso!\n")
                else:
                    utils.imprimir_italico("Mangá não encontrado!")
                utils.linha()

            # Mostra estatísticas dos mangás cadastrados
            case "STATS":
                services.mostrar_estatisticas(mangas_cadastrados)

            # Procura um mangá específico na lista
            case "SEARCH":
                services.pesquisar_manga(mangas_cadastrados)

            case _:
                utils.imprimir_italico_vermelho("Digite um comando válido!")
                utils.linha()

    utils.imprimir_italico("Programa encerrado, até logo!")
    utils.linha()


if __name__ == "__main__":
    main()
