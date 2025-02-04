import math

class Figura:
    
    def areaFig(ladoLargo, numLado):
        if numLado <= 2:
            return "Figura no válida"
        elif numLado == 3:
            altura = (ladoLargo**2 - (ladoLargo / 2)**2)**0.5
            area = (ladoLargo * altura) / 2
        elif numLado == 4:
            area = ladoLargo * ladoLargo
        else:
            area = (1 / 4) * numLado * (ladoLargo ** 2) / math.tan(math.pi / numLado)
        return area

    @staticmethod
    def perimetroFig(ladoLargo, numLado):
        perim = ladoLargo * numLado
        return perim

numLado = int(input("Ingrese la cantidad de lados en la figura: "))
ladoLargo = float(input("Ingrese la medida del lado: "))
print(f"Área de la figura: {Figura.areaFig(ladoLargo, numLado)}")
print(f"Perímetro de la figura: {Figura.perimetroFig(ladoLargo, numLado)}")
