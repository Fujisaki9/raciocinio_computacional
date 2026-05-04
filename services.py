"""Módulo de Serviços - Gestor de Mangás.

Este arquivo contém toda a lógica do programa:
- Salvamento e leitura de dados em JSON.
- Funções de cadastro, busca e listagem.
- Validações de entrada de dados."""

from time import sleep
import utils
import json


def informacoes_autor_projeto():
    utils.imprimir_italico("Gestor de Mangás do Celso Henrique Pereira Benassi.")
    utils.linha()


def encerrar_programa():
    utils.imprimir_italico("Encerrando o programa...")
    utils.linha()


def cadastrar_novos_mangas(quantidade_manga: int, mangas_cadastrados):
    for i in range(quantidade_manga):
        cadastrar_manga = utils.imprimir_negrito(f"Digite o nome do {i + 1}º mangá: ").strip().title()
        verificar_manga_cadastrado = verificar_manga_duplicado(cadastrar_manga, mangas_cadastrados)
        if verificar_manga_cadastrado:
            utils.formatar_italico(f"O mangá {cadastrar_manga} já está cadastrado\n")
        else:
            dados_manga = {
                "nome": cadastrar_manga,
                "concluido": validar_conclusao_obra(),
                "historico": []
            }
            utils.formatar_italico(f"O mangá {dados_manga['nome']} foi cadastrado com sucesso!\n")
            mangas_cadastrados.append(dados_manga)
        utils.linha()


def verificar_manga_duplicado(manga: str, lista_mangas: list) -> bool:
    verificar_manga = False
    for i in lista_mangas:
        if manga == i["nome"]:
            verificar_manga = True
            break
    return verificar_manga


def validar_conclusao_obra():
    while True:
        dados = utils.imprimir_negrito("A obra já foi concluída? [1]Sim [0]Não: ").strip()
        if dados not in ("0", "1"):
            utils.imprimir_italico_vermelho("Digite um valor entre 0 e 1!")
        else:
            dados = bool(int(dados))
            break
    return dados


def listar_projetos_cadastrados(lista_mangas_cadastrados: list):
    if len(lista_mangas_cadastrados) == 0:
        utils.imprimir_italico("Sua lista está vazia, cadastre algo nela!")
        utils.linha()
    else:
        utils.imprimir_italico("LISTA DE MANGÁS CADASTRADOS")
        for i in sorted(lista_mangas_cadastrados, key=lambda x: x['nome']):
            for k, v in i.items():
                utils.formatar_italico(f"{k.capitalize()} - {v} | ", end=' ')
            print()
        utils.linha()


def procurar_manga_na_lista(procurar_manga: str, lista_mangas_cadastrados: list):
    for manga in lista_mangas_cadastrados:
        if manga["nome"] == procurar_manga:
            return manga
    return None


def mostrar_estatisticas(lista: list):
    concluidos = nao_concluidos = 0
    lista_concluidos = list()
    lista_nao_concluidos = list()
    for i in lista:
        if i["concluido"]:
            concluidos += 1
            lista_concluidos.append(i["nome"])
        else:
            nao_concluidos += 1
            lista_nao_concluidos.append(i["nome"])
    utils.imprimir_italico(f"Mangás concluídos: {concluidos} - {lista_concluidos}")
    utils.imprimir_italico(f"Mangás não-finalizados: {nao_concluidos} - {lista_nao_concluidos}")
    utils.linha()


def pesquisar_manga(lista):
    manga = utils.imprimir_negrito("Digite o nome do mangá: ").strip().title()
    manga_lista = False
    for i in lista:
        if manga == i["nome"]:
            manga_lista = True
            break
    if manga_lista:
        utils.imprimir_italico(f"O mangá {manga} foi encontrado!")
    else:
        utils.imprimir_italico(f"O mangá {manga} não foi encontrado!")
    utils.linha()


def verificar_arquivo_json():
    lista = list()
    try:
        with open("mangas.json", "r", encoding = "utf-8") as arquivo_mangas:
            lista = json.load(arquivo_mangas)
            utils.imprimir_italico("Abrindo o arquivo...")
            sleep(1)
            utils.imprimir_italico("Arquivo carregado com sucesso!")
    except FileNotFoundError:
        utils.imprimir_italico("Abrindo o arquivo...")
        sleep(1)
        utils.imprimir_italico("Arquivo .json não encontrado")
    except json.JSONDecodeError:
        utils.imprimir_italico("Erro na execução do arquivo")
    return lista


def inserir_dados_json(lista:list):
    with open("mangas.json", "w", encoding = "utf-8") as arquivo_mangas:
            json.dump(lista, arquivo_mangas,
                      ensure_ascii = False,
                      indent = 4)