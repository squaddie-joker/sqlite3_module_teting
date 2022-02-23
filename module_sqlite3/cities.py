import sqlite3


def get_cities_from_file(f_path : str) -> set():
    with open(f_path, encoding='UTF-16') as file:
        first_line = file.readline()
        city_set = set()
        while True:
            line = file.readline()
            if (not line):
                break
            if len(line) < 3:
                continue
            city, region = line.strip().split(';')
            city_set.add((city, region))
    return city_set


def get_regions_codes_from_file(f_path : str) -> set():
    with open(f_path, encoding='UTF-16') as file:
        first_line = file.readline()
        regions_codes_set = list()
        while True:
            line = file.readline()
            if (not line):
                break
            if (len(line) < 3):
                continue
            values = line.strip().split(';')
            region_name, codes = values[0], values[1:]
            regions_codes_set.append((region_name, codes))
        return regions_codes_set


def create_connection(db_path : str) -> sqlite3.Connection:
    connection = None

    try:
        connection = sqlite3.connect(db_path)
        print("Successful connection!")
    except sqlite3.Error as err:
        print(f"Error! {err}")

    return connection 


def exequte_query(connection : sqlite3.Connection, query : str) -> bool:
    result = False

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Successful execution!")
        result = True
    except sqlite3.Error as err:
        print(f"Error execution! {err}")

    return result


def exequte_select_query(connection : sqlite3.Connection, query : str) -> list:
    result = None

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except sqlite3.Error as err:
        print(f"Error execution! {err}")

    return result

