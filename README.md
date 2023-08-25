# ETL e Carregamento de Dados dos Melhores Jogadores de CS:GO

Este projeto demonstra um exemplo prático de Extração, Transformação e Carregamento (ETL) de dados dos melhores jogadores de CS:GO a partir do arquivo CSV `hltv_playerStats-complete.csv`. Os dados extraídos são transformados para calcular estatísticas relevantes e, em seguida, carregados em um banco de dados SQLite para futuras análises e consultas.

## Descrição

O processo de ETL desempenha um papel fundamental na organização e análise de grandes volumes de dados. Neste projeto, nos concentramos nos melhores jogadores de CS:GO listados no arquivo `hltv_playerStats-complete.csv` e demonstramos como realizar o ETL para calcular e armazenar informações essenciais em um banco de dados.

## Jogadores Selecionados

- coldzera
- fallen
- s1mple
- NiKo

## Requisitos

- Python (versão utilizada: 3.6+)
- Biblioteca `sqlite3` (já incluída no Python)
- Biblioteca `csv` (já incluída no Python)

## Instruções

1. Certifique-se de ter o Python instalado. Verifique a versão instalada digitando `python --version` no terminal.

2. Clone ou faça o download deste repositório para o seu sistema local.

3. Coloque o arquivo `hltv_playerStats-complete.csv` no mesmo diretório que os arquivos do projeto.

4. Abra o terminal e navegue até o diretório do projeto.

5. Execute o script Python `etl.py` para realizar o processo de ETL. Os dados serão extraídos do arquivo CSV, transformados para calcular estatísticas relevantes e carregados no banco de dados SQLite.

6. Após a execução bem-sucedida, você pode explorar e consultar os dados diretamente no banco de dados SQLite.

## Estrutura do Projeto

- `etl.py`: O script Python que realiza o processo de Extração, Transformação e Carregamento (ETL) dos dados.
- `load.py`: O script Python que cuida do carregamento dos dados transformados no banco de dados SQLite.
- `hltv_playerStats-complete.csv`: O arquivo CSV contendo os dados dos jogadores.
- `player_stats_database.db`: O banco de dados SQLite onde os dados transformados são armazenados.
- `README.md`: Este arquivo README.

## Observações

- Este projeto é apenas um exemplo educacional e pode ser adaptado para lidar com cenários mais complexos, como múltiplas fontes de dados ou cálculos adicionais.
- Certifique-se de atualizar as configurações, consultas SQL e outros detalhes para corresponder aos seus requisitos específicos.

## Autor

Júlian Domeneghini

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

