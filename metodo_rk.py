import math

class Datos():
    def obtener_datos(self):    
        function_str = input("Ingrese una funcion: ")
        x = float(input('x: '))
        y = float(input('y: '))
        h = float(input('h: '))
        range_1 = float(input('Primer valor del rango: '))
        range_2 = float(input('Segundo valor del rango: '))
        return x , y, h, function_str, range_2

class Metodo():
    def __init__(self, datos):
        self.x = datos[0]
        self.y = datos[1]
        self.h = datos[2]
        self.f = datos[3]
        self.k1 = 0
        self.k2 = 0
        self.k3 = 0
        self.k4 = 0
        self.y_sig = None
        self.end = datos[-1]
        self.results = None

    def calculate_k1(self):
        self.k1 = self.eval_funcion(self.x , self.y)

    def calculate_k2(self):
        x = self.x + self.h/2
        y = self.y + ((self.h/2)*self.k1)
        self.k2 = self.eval_funcion(x , y)

    def calculate_k3(self):
        x = self.x + self.h/2
        y = self.y + ((self.h/2)*self.k2)
        self.k3 = self.eval_funcion(x , y)
    
    def calculate_k4(self):
        x = self.x + self.h
        y = self.y + (self.h*self.k3)
        self.k4 = self.eval_funcion(x , y)
    
    def calculate_y_sig(self):
        self.y_sig = (self.y + 1/6*(self.k1 + 2*self.k2 + 2*self.k3 + self.k4)*self.h)

    def eval_funcion(self, x , y):
        local_dict = {'x': x, 'y': y, 'math': math}
        return eval(self.f, {}, local_dict)

    def reiniciar(self):
        self.y = self.y_sig 
        self.x += self.h
    
    def ejecutar(self):
        self.calculate_k1()
        self.calculate_k2()
        self.calculate_k3()
        self.calculate_k4()
        self.calculate_y_sig()
        self.results = self.eval_funcion(self.x, self.y)
    
    def print_tabla(self):
        print('--------------------------------------------------------------------------------')
        print('|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^12}|'.format('x', 'y', 'k1', 'k2', 'k3', 'k4', 'f(x, y)'))
        print('--------------------------------------------------------------------------------')

    def print_resultados(self):
        print('|{:^10.5f}|{:^10.5f}|{:^10.5f}|{:^10.5f}|{:^10.5f}|{:^10.5f}|{:^12.5f}|'.format(self.x, self.y, self.k1, self.k2, self.k3, self.k4, self.results))

    def run(self):
        while self.x + self.h <= self.end:
            self.ejecutar()
            self.print_resultados()
            self.reiniciar()

        if self.x == self.end:
            print('|{:^10.5f}|{:^10.5f}|'.format(self.x, self.y))