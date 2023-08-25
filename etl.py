import csv
import sqlite3


# Função para extrair os dados do arquivo CSV
def extract_data(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


# Função para transformar os dados
def transform_data(data):
    transformed_data = {}
    for row in data:
        nick = row['nick']
        headshot_percentage = float(row['headshot_percentage'])

        if nick in transformed_data:
            transformed_data[nick]['total_headshot_percentage'] += headshot_percentage
            transformed_data[nick]['count'] += 1
        else:
            transformed_data[nick] = {
                'total_headshot_percentage': headshot_percentage,
                'count': 1
            }
    return transformed_data


# Função para carregar os dados transformados no banco de dados
def load_data_to_database(data, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS player_stats (
            id INTEGER PRIMARY KEY,
            nick TEXT,
            total_headshot_percentage REAL,
            count INTEGER
        )
    ''')

    for nick, stats in data.items():
        total_headshot_percentage = stats['total_headshot_percentage']
        count = stats['count']

        cursor.execute('''
            INSERT OR REPLACE INTO player_stats (nick, total_headshot_percentage, count)
            VALUES (?, ?, ?)
        ''', (nick, total_headshot_percentage, count))

    conn.commit()
    conn.close()


# Caminho para o arquivo CSV de dados
csv_file_path = 'hltv_playerStats-complete.csv'
extracted_data = extract_data(csv_file_path)
transformed_data = transform_data(extracted_data)

# Caminho para o arquivo do banco de dados SQLite
db_path = 'player_stats_database.db'
load_data_to_database(transformed_data, db_path)
