import random

NOMBRES = [
    'Ana',
    'Rogelio',
    'Alvaro',
    'Heyling',
    'Tom',
    'Maverick',
    'Roberto',
    'Josue',
    'Giselle',
    'Maria',
    'Dolores'
]

CIUDADES = [
    'Nicaragua',
    'Alemania',
    'Raccoon city',
    'Silent Hill',
    'Zurbaran',
    'Madrid'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes= {
            'Nombre': random.choice(NOMBRES),
            'Edad': random.randrange(16, 30),
            'Year en universidad': random.randrange(1, 5),
            'Cuidad': random.choice(CIUDADES)
        }
        return estudiantes

print generar_diccionario_estudiantes()