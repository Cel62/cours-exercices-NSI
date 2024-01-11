from file import *

def creer_file_vide():
    return []

def file_vide(file):
    return file == []

def enfiler(element, file):
    file.append(element)
    
def defiler(file):
    if not file_vide(file):
        file.pop(file[0])
    
def premier(file):
    if not file_vide(file):
        return file[0]

def taille(file):
    return len(file)
