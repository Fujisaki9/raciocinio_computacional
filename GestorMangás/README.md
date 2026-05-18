# 📚 Gestor de Mangás

Este projeto é um sistema de gerenciamento de coleções desenvolvido para a disciplina de **Raciocínio Computacional** do curso de **Análise e Desenvolvimento de Sistemas (ADS)** na **PUCPR**. O objetivo é gerenciar uma coleção pessoal de mangás através do terminal, com persistência de dados em JSON.

## 🛠️ Tecnologias e Bibliotecas utilizadas
* **Linguagem**: Python 3
* **Bibliotecas**: `json` (persistência de dados), `time` (controle de fluxo), `rich` (formatação visual), `datetime` (manipulação de datas)
* **Ambiente**: PyCharm

## 📋 Lista de Comandos e Funcionalidades

| Comando | Ação | Descrição |
| :--- | :--- | :--- |
| `ADD` | Cadastrar | Inicia o cadastro de novos mangás, solicitando o nome e status. |
| `LIST` | Listar | Exibe uma lista organizada com todos os itens cadastrados. |
| `UPDATE` | Alterar | Permite localizar um mangá específico e alterar suas informações. |
| `DELETE` | Remover | Remove um mangá específico da sua lista. |
| `STATS` | Estatísticas | Gera um resumo estatístico mostrando quantos mangás estão concluídos e quantos ainda estão em andamento. |
| `SEARCH` | Buscar | Verifica se um título específico já existe na coleção. |
| `ABOUT` | Informações | Exibe as informações do projeto e do desenvolvedor. |
| `QUIT` | Sair | Salva as alterações no arquivo `mangas.json` e encerra o programa. |

## 🚀 Como Executar
1. Certifique-se de ter o **Python** instalado.
2. Clone o repositório ou baixe os arquivos `main.py`, `services.py` e `utils.py`.
3. Instale as dependências: `-pip install rich`.
4. ⚠️ **PyCharm:** Habilite *Emulate terminal in output* em `Run > Edit configurations > Edit configuration templates > Python > Modify options` para visualizar a interface colorida.

---
Desenvolvido por **Celso Henrique Pereira Benassi**.
