from poblacion_csv import utilidades

def get_porcentaje_mundial(lista_paises):
    data_porcentaje = {}
    pais = ""
    for elem in lista_paises:
        for key, value in elem.items(): 
            if(key == "Country/Territory"):
                pais = value      
            if (key == "World Population Percentage"):
                data_porcentaje[pais] = value
    return data_porcentaje

if __name__ == "__main__" :
    data = utilidades.get_datos("./poblacion_csv/data.csv")
    porcentaje = get_porcentaje_mundial(data)
    

