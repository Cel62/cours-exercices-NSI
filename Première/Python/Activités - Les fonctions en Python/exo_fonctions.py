def carre(n):
    """Une fonction qui fait le carré d'un entier
    :param n: entier à mettre au carré
    :type n: int
    :return: le carre d'un entier
    :rtype: int
    :Example:
    >>> carre(2)
    4
    >>> carre(3)
    9
    >>> carre(-4)
    16
    """
    return n * n


def polynome(x):
    """Une fonction qui retourne le résultat du calcul de x^2 + 2x + 10 sous forme d'un entier
    :param x: entier
    :type x: int
    :return: le résultat du calcul de x^2 + 2x + 10
    :rtype: int
    :Example:
    >>> polynome(0)
    10
    >>> polynome(-1)
    9
    >>> polynome(1)
    13
    """
    return x**2 + 2*x + 10


def polynome2(a, b, c, x):
    """Une fonction qui retourne le résultat de a*x^2 + b*x + c
    :param a: entier
    :param b: entier
    :param c: entier
    :param x: flottant
    :type a: int
    :type b: int
    :type c: int
    :type x: float
    :return: le résultat de a*x^2 + b*x + c
    :rtype: float
    :Example:
    >>> polynome2(1, 1, 1, 1)
    3
    >>> polynome2(-1, -1, -1 ,-1)
    -1
    >>> polynome2(5, -7, 6, 5.5)
    118.75
    """
    return a*x**2 + b*x + c


def celcius_to_fahrenheit(temp_celcius):
    """Une fonction qui convertit une température en celcius vers une température en fahrenheit
    :param temp_celcius: température en celcius
    :type temp_celcius: float
    :return: la température en fahrenheit
    :rtype: float
    :Example:
    >>> celcius_to_fahrenheit(2)
    35.6
    >>> celcius_to_fahrenheit(3)
    37.4
    >>> celcius_to_fahrenheit(-4)
    24.8
    """
    return (temp_celcius * 9/5) + 32

def fahrenheit_to_celcius(temp_fahrenheit):
    """Une fonction qui convertit une température en fahrenheit vers une température en celcius
    :param temp_fahrenheit: température en fahrenheit
    :type temp_fahrenheit: float
    :return: la température en celcius
    :rtype: float
    :Example:
    >>> fahrenheit_to_celcius(35.6)
    2
    >>> fahrenheit_to_celcius(37.4)
    3
    >>> fahrenheit_to_celcius(24.8)
    -4
    """
    return round((temp_fahrenheit - 32) * 5/9)
    
def surface_disque(r, unite):
    """Une fonction qui renvoie la surface du disque en précisant l'unité utilisée
    :param r: le rayon du disque
    :param unite: l'unité a utilisé (m, cm, mm)
    :type r: float
    :type unite: string
    :return: la surface du disque avec l'unité
    :rtype: string
    :Example:
    >>> surface_disque(1, "mm")
    'La surface du disque est de 3.14 mm carré'
    >>> surface_disque(2, "cm")
    'La surface du disque est de 12.57 cm carré'
    >>> surface_disque(3, "m")
    'La surface du disque est de 28.27 m carré'
    """
    from math import pi
    resultat = round(pi * r**2, 2)
    return 'La surface du disque est de ' + str(resultat) + ' ' + unite + ' carré'

def parite(n):
    """Une fonction qui prend un nombre entier n et retourne un booléen si n est pair
    :param n: nombre entier
    :type n: int
    :return: booléen si n est pair/impair
    :rtype: bool
    :Example:
    >>> parite(1)
    False
    >>> parite(2)
    True
    >>> parite(50)
    True
    """
    isinstance(n, int)
    return n % 2 == 0

def tirage_au_sort(a, b):
    """Une fonction qui renvoie 5 nombres entiers au hasard entre un nombre a et b.
    :param a: nombre entier
    :param b: nombre entier
    :type a: int
    :type b: int
    :return: 5 nombres entiers au hasard
    :rtype: int
    :Example:
    >>> tirage_au_sort(1, 10)
    
    >>> tirage_au_sort(2, 25)
    
    >>> tirage_au_sort(10, 100)
    
    """
    isinstance(a, int)
    from random import randint
    return randint(a, b), randint(a, b), randint(a, b), randint(a, b), randint(a, b)
    
import doctest
doctest.testmod(verbose = True)