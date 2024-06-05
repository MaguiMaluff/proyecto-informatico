import math

class Datos():
    def obtener_datos(self):    
        function_str = input("Ingrese una funcion: ")
        x = input('x: ')
        y = input('y: ')
        return x , y , function_str

class Function():
    def eval_funcion(self, datos):
        x = int(datos[0])
        y = int(datos[1])
        function_str = datos[2]
        context = {'x': x, 'y': y, 'math': math}
        z = eval(function_str, {"__builtins__": None}, context)
    
class Metodo():
    


if __name__ == '__main__':
    datos = Datos()
    datitos = datos.obtener_datos()
    fun = Function()
    fun.eval_funcion(datitos)
