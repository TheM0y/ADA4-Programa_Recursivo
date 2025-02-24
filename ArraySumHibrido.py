import time

def promedio_iterativo(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def promedio_recursivo(numeros, n=None):
    if n is None:
        n = len(numeros)
    if n == 0:
        return 0
    return (numeros[n - 1] + (n - 1) * promedio_recursivo(numeros, n - 1)) / n

def main():
    numeros = []
    while True:
        try:
            cantidad = int(input("¿Cuántos números desea ingresar?: "))
            if cantidad < 0:
                print("Introduzca un número entero positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Introduzca un número entero.")
    
    for _ in range(cantidad):
        while True:
            try:
                numero = float(input("Introduzca un número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Introduzca un número válido.")
    
    if numeros:
        inicio_iter = time.time()
        promedio_it = promedio_iterativo(numeros)
        fin_iter = time.time()
        
        inicio_rec = time.time()
        promedio_rec = promedio_recursivo(numeros)
        fin_rec = time.time()
        
        print(f"Promedio Iterativo: {promedio_it} (Tiempo: {fin_iter - inicio_iter:.6f} segundos)")
        print("Complejidad promedio_iterativo: O(n)")
        
        print(f"Promedio Recursivo: {promedio_rec} (Tiempo: {fin_rec - inicio_rec:.6f} segundos)")
        print("Complejidad promedio_recursivo: O(n^2)")
    else:
        print("No se ingresaron números.")

if __name__ == "__main__":
    main()
