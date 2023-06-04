import csv

def get_datos(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []
        for fila in reader:
            iterable = zip(header, fila)
            pais_dic = {key:value for key, value in iterable}
            data.append(pais_dic)
    return data

def separa_dicc(datos):
    keys = datos.keys()
    values = datos.values()
    return keys, values