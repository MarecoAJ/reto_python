from poblacion_csv import utilidades

def get_pais(lista_paises, pais):
    data_pais = {}
    for elem in lista_paises:
        for key, value in elem.items():      
            if (key == "Country/Territory"):
                if(value == pais):
                    data_pais = elem
    return data_pais

def get_poblacion(pais):
    poblacion = {
        "2022" : int(pais["2022 Population"]),
        "2020": int(pais["2020 Population"]),
        "2015": int(pais["2015 Population"]),
        "2010": int(pais["2010 Population"]), 
        "2000": int(pais["2000 Population"]), 
        "1990": int(pais["1990 Population"]), 
        "1980": int(pais["1980 Population"]), 
        "1970": int(pais["1970 Population"]) 
        }
    labels = poblacion.keys()
    values = poblacion.values()
    return labels, values

if __name__ == "__main__" :
    data = utilidades.get_datos("./poblacion_csv/data.csv")
    pais = get_pais(data, "Argentina")
    poblacion = get_poblacion(pais)
