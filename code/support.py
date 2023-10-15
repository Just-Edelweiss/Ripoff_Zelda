from csv import reader

def import_csv_layout(chemin):
    terrain = []
    with open(chemin) as map_level:
        layout = reader(map_level, delimiter = ',')
        for ligne in layout:
            terrain.append(list(ligne))
    return terrain

print(import_csv_layout('assets/map/Zeldouille_map._barrier.csv'))