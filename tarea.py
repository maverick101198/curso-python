

if __name__ == '__main__':
    nombre = input("Digita el nombre: ")
    edad = int(input("Digite su edad: "))
    dato = 100 - edad
    cumplira = 2017 + dato

    mensaje = "<< {nombre} >>, cumplira 100 años en: {anio}"

    print(mensaje.format(nombre=nombre, anio=cumplira))
