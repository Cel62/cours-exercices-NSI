// Dimensions pour les affichages
let padding = 10
let box_size = 25
let separation = 2
let hauteur_ligne = box_size + separation
let largeur_canvas = 0

// Position du curseur
let position = 0
let positions = []

// l'objet qui stockera les décalages
let occurences = new Map()
let faux_caractere = ""
let faux_indice = 0

// Décompte du nombre de comparaisons effectuées
let comparaisons = 0
let comparaisons_total = new Map()
comparaisons_total.set(-1, 0)

// Les couleurs (vides car initialisées dans le setup mais gagnent ainsi une portée globale)
let correct = null
let incorrect = null
let neutre = null
let saut = null

// Le contenu du texte et du motif (vide pour être globaux)
let texte = null
let motif = null

function setup() {
    /*
    Initialisation de P5J :
    - Dimensionnement du canvas
    - Création des couleurs
    */
    let canvasDiv = $("#canvas")
    largeur_canvas = canvasDiv.width()
    createCanvas(largeur_canvas, 300);

    correct = color(74, 216, 69)
    incorrect = color(229, 78, 55)
    neutre = color(220)
    saut = color(249, 223, 144)
}

function position_droite() {
    /*
    Déplacement vers la droite, MAJ de la position du curseur avec l'algorithme de Boyer-Moore
    */
    if (occurences.has(faux_caractere)) {
        position += max(faux_indice - occurences.get(faux_caractere), 1)
    } else {
        position += faux_indice + 1
    }
    dessiner()
}

function render_char(c, x, y, color) {
    /*
    Affichage d'un caractère à la position (x,y) et selon la couleur passée en argument
    - Dessin d'un rectangle de la couleur indiquée
    - Affichage du caractère
    */
    fill(color)
    rect(x, y, box_size, box_size)
    fill(0)
    textSize(box_size)
    textAlign(LEFT, TOP);
    text(c, x + separation, y)
}

function creation_occurences(motif) {
    /*
    Création de la liste caractère -> dernière occurence dans le motif
    */
    occurences = new Map()

    for (let i = 0; i < motif.length; i++) {
        occurences.set(motif.charAt(i), i)
    }
}

function lancer() {
    /*
    Exécution du bouton : remise à zéro de la position du curseur, MAJ du texte et du motif, calcul des occurences et dessin
    */
    position = 0

    // Activation du bouton
    $("#right-button").prop('disabled', false)
    $("#right-button").removeClass("btn-secondary")
    $("#right-button").addClass("btn-info")

    // Récupération des contenus des inputs
    texte = $("#texte").val()
    motif = $("#motif").val()

    // Calcul des occurences
    creation_occurences(motif)

    comparaisons_total = new Map()
    comparaisons_total.set(-1, 0)

    dessiner()
}

function dessiner() {
    /*
    Dessin du canvas
    */

    // On efface le canvas
    clear()

    // Variable utilisée pour les affichages
    let ligne = 0

    // Description du problème
    textAlign(LEFT, TOP);
    textSize(box_size)
    fill(0)
    text("Longueur du texte : " + texte.length, padding, padding + ligne * hauteur_ligne)
    ligne++

    text("Longueur du motif : " + motif.length, padding, padding + ligne * hauteur_ligne)
    ligne++

    // Affichage des caractères du texte
    for (let i = 0; i < texte.length; i++) {
        ligne = 3
        // Affichage des indices au dessus du texte
        textSize(box_size / 2)
        fill(60)
        text(i, padding + i * box_size, padding + ligne * hauteur_ligne + padding)
        ligne++
        render_char(texte.charAt(i), padding + i * box_size, padding + ligne * hauteur_ligne, neutre)
    }

    // Booléen indiquant si les caractères précédemment testés correspondaient
    enCours = true
    // Booléen utilisé pour mettre en évidence un caractère correspondant dans le motif
    trouve = false
    // Stockage du caractère incorrect dans le texte et de la position concernée dans le motif
    faux_caractere = ""
    faux_indice = 0
    // Nombre de comparaisons effectuées ce tour-ci
    comparaisons = 0

    // Affichage du motif 
    if (position <= texte.length - motif.length) {
        // La couleur du rectangle (vert, rouge ou gris selon la comparaison entre le texte et le motif)
        for (let j = motif.length - 1; j > -1; j--) { // on part de la fin du motif et on remonte
            couleur = neutre
            if (enCours) {
                comparaisons++
                if (motif.charAt(j) == texte.charAt(position + j)) { // correspondance
                    couleur = correct
                } else { // pas de correspondance
                    couleur = incorrect
                    faux_caractere = texte.charAt(position + j)
                    faux_indice = j
                    enCours = false
                }
                if ((enCours) && (j == 0)) { // On a trouvé une correspondance parfaite
                    // Déactivation du bouton
                    $("#right-button").prop('disabled', true)
                    $("#right-button").addClass("btn-secondary")
                    $("#right-button").removeClass("btn-info")
                }
            }

            ligne = 4
            // Affichage du caractère du texte
            render_char(texte.charAt(position + j), padding + (position + j) * box_size, padding + ligne * hauteur_ligne, couleur)
            // Affichage du caractère du motif
            ligne++
            if ((!trouve) && (motif.charAt(j) == faux_caractere)) { // mise en évidence d'un caractère du motif qui pourrait correspondre au caractère du texte
                couleur = saut
                trouve = true
            }
            render_char(motif.charAt(j), padding + (position + j) * box_size, padding + ligne * hauteur_ligne, couleur)
            ligne++

            // Affichage de l'indice dans le motif
            textSize(box_size / 2)
            fill(60)
            text(j, 10 + (position + j) * box_size, padding + ligne * hauteur_ligne)
        }
    }

    // MAJ du nombre total de comparaisons effectuées
    if (comparaisons_total.has(position) == false) {
        last = 0
        for (let v of comparaisons_total.values()) {
            last = v
        }
        comparaisons_total.set(position, last + comparaisons)
    }

    // Affichage des nombres de comparaisons
    textSize(box_size)
    fill(0)
    ligne = 0
    text("Nombres de comparaisons (ce tour) : " + comparaisons, padding + 2 * largeur_canvas / 5, padding + ligne * hauteur_ligne)
    ligne++
    text("Nombres de comparaisons (total) : " + comparaisons_total.get(position), padding + 2 * largeur_canvas / 5, padding + ligne * hauteur_ligne)

    // Affichage des dernières occurences dans le motif
    ligne = 8
    text("Dernière occurrence des caractères dans le motif :", padding, padding + ligne * hauteur_ligne)
    ligne++
    i = 0
    textSize(box_size)
    fill(0)
    for (let [key, value] of occurences) {
        couleur = neutre
        if (faux_caractere == key) {
            couleur = saut
        }
        render_char(key, padding + i * box_size, padding + ligne * hauteur_ligne, couleur)
        text(value, padding + (i + 2) * box_size, padding + ligne * hauteur_ligne)
        i = i + 4
    }

}