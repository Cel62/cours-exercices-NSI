scrabble = {"A": [1, 9],
            "B": [3, 2],
            "C": [3, 2],
            "D": [2, 3],
            "E": [1, 15],
            "F": [4, 2],
            "G": [2, 2],
            "H": [4, 2],
            "I": [1, 8],
            "J": [8, 1],
            "K": [10, 1],
            "L": [1, 5],
            "M": [2, 3],
            "N": [1, 6],
            "O": [1, 6],
            "P": [3, 2],
            "Q": [8, 1],
            "R": [1, 6],
            "S": [1, 6],
            "T": [1, 6],
            "U": [1, 6],
            "V": [4, 2],
            "W": [10, 1],
            "X": [10, 1],
            "Y": [10, 1],
            "Z": [10, 1]
            }

def score(mot):
    points = 0
    for lettre in mot:
        points = points + scrabble.get(lettre)[0]
    return points

def tirage_au_sort():
    import random
    lettre = choice(list(scrabble.keys()))
    