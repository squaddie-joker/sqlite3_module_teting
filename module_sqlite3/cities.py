def get_cities_from_file(f_path):
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

F_PATH = r'c:\Users\laa45\Downloads\spisok.csv'
city_set = get_cities_from_file(F_PATH)

for item in city_set:
    print(item)

