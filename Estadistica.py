class Estadistica:
    def stats(self, cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            suma = sum(map(int, numeros))
            return [len(numeros), int(min(numeros)), int(max(numeros)), suma/float(len(numeros))]
        else:
            return [int(cadena), int(cadena), int(cadena), int(cadena)]

