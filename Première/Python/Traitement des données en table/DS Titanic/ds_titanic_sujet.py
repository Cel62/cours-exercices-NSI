# L'exercice se base sur le titanic.csv dans le lequel se trouve des informations sur une partie des passagers du Titanic

# Préséntation du fichier csv utilisé :
#	* Le séparateur de données est la tabulation (Attention, ici de ne pas sélectionner la virgule comme séparateur à l'ouverture avec un tableur).
#	* Les descripteurs sont :
#		* name : nom du passager.
#		* gender : sexe du passager (male ou female).
#		* age : age du passager.
#		* class : 1st, 2nd ou 3rd (première classe, seconde classe ou troisième classe) ou fonction à bord.
#		* embarked : Port d'embarcation (C = Cherbourg, Q = Queenstown, S = Southampton).
#		* country : pays d'origine
#		* ticketno : numéro (code) du ticket passager.
#		* fare : prix du ticket.
#		* sibSp : nombre de frères, soeurs (et conjoints) sur le bateau.
#		* parch: nombre de parents et enfants sur le bateau.
#		* survived : personne survivant ou non (yes ou no)

import csv

def lecture(fichier_csv) :
    ''' fonction qui prend un argument 'fichier_csv' qui est un fichier csv et qui renvoie une liste de dictionnaires
    >>> lecture('titanic.csv')[0]
    {'name': 'Abbing, Mr. Anthony', 'gender': 'male', 'age': '42', 'class': '3rd', 'embarked': 'S', 'country': 'United States', 'ticketno': '5547', 'fare': '7.11', 'sibsp': '0', 'parch': '0', 'survived': 'no'}
    '''
    with open(fichier_csv, "r", encoding='utf-8') as csvfich:
        reader = csv.DictReader(csvfich, delimiter=',')
        data = [dict(ligne) for ligne in reader]
        return data
    
donnees = lecture('titanic.csv')

def passagers():
    ''' fonction sans argument qui retourne la liste complète des noms des passagers et membres d'équipages
    >>> passagers()[25]
    'Allison, Mrs. Bessie Waldo'
    >>> passagers()[12]
    'Ahlin, Mrs. Johanna Persdotter'
    ''' 
    return [personnes['name'] for personnes in donnees]

def passagers_genre(genre):
    ''' fonction qui prend un argument 'genre' qui peut prendre deux valeurs 'male' ou 'female' et
    qui retourne la liste complète des noms des passagers et membres d'équipages en fonction du genre
    >>> passagers_genre('male')[1]
    'Abbott, Mr. Eugene Joseph'
    >>> passagers_genre('female')[1]
    'Abelseth, Miss. Karen Marie'
    '''
    return [personnes['name'] for personnes in donnees if personnes['gender'] == genre]

def survivants():
    ''' fonction sans argument qui retourne la liste complète des noms des passagers et membres d'équipages qui ont survécu
    >>> survivants()[0]
    "Abbott, Mrs. Rhoda Mary 'Rosa'"
    >>> survivants()[1]
    'Abelseth, Miss. Karen Marie'
    '''
    return [personnes['name'] for personnes in donnees if personnes['survived'] == 'yes']

def survivants_genre(genre):
    ''' fonction qui prend un argument 'genre' qui peut prendre deux valeurs 'male' ou 'female' et
    qui retourne la liste complète des noms des passagers et membres d'équipages survivants en fonction du genre
    >>> survivants_genre('male')[0]
    'Abelseth, Mr. Olaus Jørgensen'
    >>> survivants_genre('female')[0]
    "Abbott, Mrs. Rhoda Mary 'Rosa'"
    '''
    return [personnes['name'] for personnes in donnees if personnes['gender'] == genre and personnes['survived'] == 'yes']

def survivants_age(age):
    ''' fonction qui prend un argument 'age' qui peut prendre un entier et qui retourne la liste complète des noms des
    passagers et membres d'équipages survivants qui ont un age supérieur à celui passé en paramètre
    >>> survivants_age(50)[0]
    'Andrews, Miss. Kornelia Theodosia'
    >>> survivants_age(60)[1]
    'Bonnell, Miss. Elizabeth'
    '''
    return [personnes['name'] for personnes in donnees if personnes['survived'] == 'yes' and float(personnes['age']) > age]

def survivants_classe(classe):
    ''' fonction qui prend un argument 'classe' qui prendre les valeurs 1st 2nd 3rd et qui retourne la liste des noms
    des survivants en fonction de leur classe
    >>> survivants_classe('1st')[12]
    'Beckwith, Mrs. Sallie'
    >>> survivants_classe('2nd')[8]
    'Becker, Mrs. Nellie E.'
    >>> survivants_classe('3rd')[5]
    'Aks, Master. Frank Philip'
    '''
    return [personnes['name'] for personnes in donnees if personnes['class'] == classe and personnes['survived'] == 'yes']

def survivants_pays(pays):
    ''' fonction qui prend un argument 'pays' qui prendre comme valeur le nom d'un pays et qui retourne la liste des
    passagers et membre d'équipages ayant la nationalité passée en argument et ayant survécus
    Exemples :
    >>> survivants_pays('France')[5]
    'Leroy, Miss. Berthe'
    >>> survivants_pays('England')[35]
    'Davison, Mrs. Mary Elizabeth'
    '''
    return [personnes['name'] for personnes in donnees if personnes['survived'] == 'yes' and personnes['country'] == pays]
    
def pourcentage_survivants_classe(classe):
    ''' fonction qui prend un argument 'classe' qui prendre les valeurs 1st 2nd 3rd et qui retourne une tuple composé de
    3 valeurs : le nb de survivants, le nb de passagers, le rapport entre nb de survivants et de passagers
    >>> pourcentage_survivants_classe('1st')
    (201, 2207, 9.107385591300408)
    >>> pourcentage_survivants_classe('2nd')
    (118, 2207, 5.346624376982329)
    >>> pourcentage_survivants_classe('3rd')
    (181, 2207, 8.201178069777978)
    >>> pourcentage_survivants_classe('deck crew')
    (43, 2207, 1.9483461712732213)
    '''
    nb_survivants = 0
    nb_passagers = 0
    rapport_nb = 0
    for personnes in donnees:
        if personnes['class'] == classe and personnes['survived'] == 'yes':
                nb_survivants = nb_survivants + 1
        nb_passagers = nb_passagers + 1
        rapport_nb = (nb_survivants / nb_passagers) * 100
    return (nb_survivants, nb_passagers, rapport_nb)


import doctest
doctest.testmod(verbose = True)