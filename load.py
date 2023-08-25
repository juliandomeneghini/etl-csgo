import sqlite3

# Caminho para o arquivo do banco de dados SQLite
db_path = 'player_stats_database.db'

# Função para visualizar os dados dos jogadores


def view_player_data(database_path, players):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    for player in players:
        cursor.execute('SELECT * FROM player_stats WHERE nick=?', (player,))
        row = cursor.fetchone()
        if row:
            print("Player:", row[1])
            print("Total Headshot Percentage:", row[2])
            print("Count:", row[3])
            print()

    conn.close()

# Jogadores específicos


specific_players = ['coldzera', 'FalleN', 's1mple', 'NiKo']

# Chama a função para visualizar os dados dos jogadores
view_player_data(db_path, specific_players)
