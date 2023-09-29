lettreADN = ['A', 'C', 'G', 'T']

def estADN(nucleotide):
    """
    Vérifie si la chaîne de caractères passée en paramètre ne contient aucun autre caractère que les quatre bases A, C, G et T
    :param nucleotide: Chaîne de caractère qui doit être A, C, G ou T
    :type nucleotide: string
    :return: Renvoie la valeur `True` si la chaîne de caractère est A, C, G ou T et renvoie la valeur `False` dans le cas contraire.
    De plus, elle renvoie `True` si la chaîne est vide
    :rtype: bool
    :Example:
    >>> estADN('ACGT')
    True
    >>> estADN('eutb')
    False
    >>> estADN('')
    True
    """
    for lettre in nucleotide:
        if lettre not in lettreADN:
            return False
    return True


def genereADN(taille):
    """
    Renvoie une séquence ADN générée aléatoirement et dont la taille est passée en paramètre
    :param taille: la taille
    :type taille: int
    :return: Renvoie une séquence ADN générée aléatoirement
    :rtype: str
    """
    from random import choice
    chaine1 = ''
    for _ in range(taille):
        chaine1 += choice(lettreADN)
    return chaine1


def baseComplementaire(lettre, sequence):
    """
    Renvoie la base complémentaire de la base passée en paramètre, selon le type de séquence demandé en
    sortie qui peut être soit 'ADN', soit 'ARN'
    :param lettre: la base
    :param sequence: le type de séquence demandé
    :type lettre: string
    :type sequence: string
    :return: Renvoie la base complémentaire
    :rtype: string
    :Example:
    >>> baseComplementaire('G', 'ADN')
    'C'
    >>> baseComplementaire('A', 'ARN')
    'U'
    """
    adnComplementaire = { "A": "T",
                          "T": "A",
                          "G": "C",
                          "C": "G"
                        }

    arnComplementaire = { "A": "U",
                          "T": "A",
                          "G": "C",
                          "C": "G"
                        }

    if lettre in lettreADN:
        if sequence == "ADN":
            complementaire = adnComplementaire.get(lettre)
            return complementaire
        elif sequence == "ARN":
            complementaire = arnComplementaire.get(lettre)
            return complementaire
    return False


def transcrit(adn, pos1, pos2):
    """
    Renvoie l'ARN construit à partir de la sous-séquence d'ADN comprise entre les deux positions passées
    en paramètre, incluses
    :param adn: la sous-séquence d'ADN
    :param pos1: position 1
    :param pos2: position 2
    :type adn: string
    :type pos1: int
    :type pos2: int
    :return: Renvoie l'ARN construit à partir de la sous-séquence d'ADN
    :rtype: string
    :Example:
    >>> transcrit('TTCTTCTTCGTACTTTGTGCTGGCCTCCACACGATAATCC', 4, 23)
    'AAGAAGCAUGAAACACGACC'
    """
    chaine = ''
    for i in range(pos1 - 1, pos2):
        chaine += baseComplementaire(adn[i], "ARN")
    return chaine


def codeGenetique(codon):
    """
    Renvoie l'acide aminé (sous la forme du nom abrévié EN 1 lettre) correspondant au codon passé en paramètre,
    ou * pour les codons Stop
    :param codon: la sous-séquence d'ADN
    :type codon: string
    :return: Renvoie l'acide aminé
    :rtype: string
    :Example:
    >>> codeGenetique('UUU')
    'F'
    >>> codeGenetique('UUA')
    'L'
    >>> codeGenetique('UAA')
    '*'
    """
    codeGen = { 'UUU': 'F', 'UUC': 'F',
                'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
                'AUG': 'M',
                'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
                'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                'UAU': 'Y', 'UAC': 'Y',
                'UAA': '*', 'UAG': '*', 'UGA': '*',
                'CAU': 'H', 'CAC': 'H',
                'CAA': 'Q', 'CAG': 'Q',
                'AAU': 'N', 'AAC': 'N',
                'AAA': 'K', 'AAG': 'K',
                'GAU': 'D', 'GAC': 'D',
                'GAA': 'E', 'GAG': 'E',
                'UGU': 'C', 'UGC': 'C',
                'UGG': 'W',
                'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
                'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
              }
    if codon in codeGen:
        return codeGen.get(codon)


def traduit(sequence):
    """
    Construit la séquence protéique obtenue par la traduction de la séquence ARN passée en paramètre. Cette
    traduction se fait à partir du premier nucléotide de la séquence ARN et utilise la fonction codeGenetique.
    :param sequence: la séquence d'ADN
    :type codon: string
    :return: Renvoie la séquence protéique
    :rtype: string
    :Example:
    >>> traduit('AUGCGAAGCCGAAAGAACACCGGCUAA')
    'MRSRKNTG*'
    """
    sequence_modifie = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        acide_amine = codeGenetique(codon)
        sequence_modifie += acide_amine
    return sequence_modifie


def replique(sequence):
    """
    Construit la séquence ADN complémentaire et inversée de celle passée en paramètre. Pour cela, cette fonction fait appel à la fonction `baseComplementaire`.
    Une contrainte d'utilisation de cette fonction est que son paramètre est bien une séquence ADN.
    :param adn: la séquence d'ADN
    :type codon: string
    :return: Renvoie la séquence ADN complémentaire et inversée
    :rtype: string
    :Example:
    >>> replique('ACTG')
    'CAGT'
    """
    adn_complementaire = ""
    for i in range(len(sequence)-1, -1, -1):
        adn_complementaire += baseComplementaire(sequence[i], 'ADN')
    return adn_complementaire
    
import doctest
doctest.testmod(verbose = True)