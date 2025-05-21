from math import pi, tan

class Figura:
    
    def areaFig(ladoLargo, numLado):
        area = (1 / 4) * numLado * (ladoLargo ** 2) / tan(pi / numLado)
        return area

    def perimetroFig(ladoLargo, numLado):
        perim = ladoLargo * numLado
        return perim

numLado = int(input("Ingrese la cantidad de lados en la figura: "))
ladoLargo = float(input("Ingrese la medida del lado: "))
if numLado <= 2 or ladoLargo <=0:
    print("Figura no válida")
else:
    print(f"Área de la figura: {Figura.areaFig(ladoLargo, numLado)}")
    print(f"Perímetro de la figura: {Figura.perimetroFig(ladoLargo, numLado)}")

