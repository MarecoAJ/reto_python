from poblacion_csv import grafico as graf
from poblacion_csv import get_poblacion_csv as pobl
from poblacion_csv import utilidades as util
from poblacion_csv import get_porcentaje_mundial as porc

def ejecutar():
    data = util.get_datos("./poblacion_csv/data.csv")
    pais = pobl.get_pais(data, "Argentina") 
    data_porcentaje = porc.get_porcentaje_mundial(data)

    if(len(pais) > 0 ):
        labels, values = pobl.get_poblacion(pais)
        graf.grafico_barra(labels, values)

    if( len(data_porcentaje) > 0):
        labels, values = util.separa_dicc(data_porcentaje)
        graf.grafico_torta(labels, values)   

if __name__ == "__main__":
    ejecutar()