from file import *

def creer_file_vide():
    return []

def file_vide(file):
    return file == []

def enfiler(element, file):
    file.insert(0, element)
    
def defiler(file):
    if not file_vide(file):
        file.remove(file[-1])
    
def premier(file):
    if not file_vide(file):
        return file[-1]

def taille(file):
    return len(file)