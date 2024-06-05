from metodo_rk import Function, Datos

def main():
    print('Método de Runge Kutta de 4to orden')
    print('Indicaciones de uso:')
    print('El programa va a pedirle 4 datos: la función, el valor de x0, y0 y h.')
    print('Para la función, tenga en cuenta ciertos criterios:')
    print('  - e = math.e')
    print('  - Raíz cuadrada: math.sqrt(x o y)')
    print('  - Logaritmo: math.log(x)')
    print('  - Exponencial: math.exp(x)')
    print('  - Seno: math.sin(x)')
    print('  - Coseno: math.cos(x)')
    print('  - Pi: math.pi')
    print('  - Los ángulos se evalúan en radianes')

    datos = Datos()
    datitos = datos.obtener_datos()
    

if __name__ == "__main__":
    main()