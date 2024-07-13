// Dimensions pour les affichages
let padding = 10
let box_size = 25
let separation = 2
let hauteur_ligne = box_size + separation
let largeur_canvas = 0

// Position du curseur
let position = 0

// Décompte du nombre de comparaisons effectuées
let comparaisons = 0
let comparaisons_total = [0]

// Les couleurs (vides car initialisées dans le setup mais gagnent ainsi une portée globale)
let correct = null
let incorrect = null
let neutre = null

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
    createCanvas(largeur_canvas, 200);

    correct = color(74, 216, 69)
    incorrect = color(229, 78, 55)
    neutre = color(220)
}

function position_gauche() {
    /*
    Déplacement vers la gauche, MAJ de la position du curseur
    */
    position = max(0, position - 1)
    dessiner()
}

function position_droite() {
    /*
    Déplacement vers la droite, MAJ de la position du curseur
    */
    texte = $("#texte").val()
    motif = $("#motif").val()
    position = min(texte.length - motif.length, position + 1)
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

function lancer() {
    /*
    Exécution du bouton : remise à la zéro de la position du curseur et dessin
    */
    position = 0

    // Activation des boutons
    $("#left-button").prop('disabled', false)
    $("#right-button").prop('disabled', false)
    $("#left-button").removeClass( "btn-secondary" )
    $("#left-button").addClass( "btn-info" )
    $("#right-button").removeClass( "btn-secondary" )
    $("#right-button").addClass( "btn-info" )

    // Récupération des contenus des inputs
    texte = $("#texte").val()
    motif = $("#motif").val()

    comparaisons_total = [0]
    dessiner()
}

function dessiner() {
    /*
    Dessin du canvas
    */

    // On efface le canvas
    clear()

    // Création de variables locales
    let ligne = 0
    comparaisons = 0
    // Booléen indiquant si les caractère précédemment testés correspondaient
    enCours = true

    // Description du problème
    textAlign(LEFT, TOP);
    textSize(box_size)
    fill(0)
    text("Longueur du texte : " + texte.length, padding, padding + ligne * hauteur_ligne)
    ligne++

    text("Longueur du motif : " + motif.length, padding, padding + ligne * hauteur_ligne)
    ligne++

    // Affichage des caractères
    for (let i = 0; i < texte.length; i++) {
        ligne = 3

        // Affichage des indices au dessus du texte
        textSize(box_size / 2)
        fill(60)
        text(i, padding + i * box_size, padding + ligne * hauteur_ligne + padding)
        ligne++

        if ((i >= position) && (i < position + motif.length)) { // un caractère du motif est situé sous ce caractère

            // La couleur du rectangle (vert, rouge ou gris selon la comparaison entre le texte et le motif)
            couleur = neutre
            if (enCours) {
                if (texte.charAt(i) == motif.charAt(i - position)) {
                    couleur = correct
                } else {
                    couleur = incorrect
                    enCours = false
                }
                comparaisons++
            }

            // Affichage du caractère du texte
            render_char(texte.charAt(i), padding + i * box_size, padding + ligne * hauteur_ligne, couleur)
            ligne++
            // Affichage du caractère du motif
            render_char(motif.charAt(i - position), padding + i * box_size, padding + ligne * hauteur_ligne, couleur)
            ligne++

            // Affichage de l'indice dans le motif
            textSize(box_size / 2)
            fill(60)
            text(i - position, 10 + i * box_size, padding + ligne * hauteur_ligne)

        } else { // le motif n'est pas sous cette zone
            render_char(texte.charAt(i), padding + i * box_size, padding + ligne * hauteur_ligne, neutre)
        }
    }

    if (position>=comparaisons_total.length-1) {
        comparaisons_total.push(comparaisons_total[comparaisons_total.length - 1] + comparaisons)
        console.log(comparaisons_total)
    }

    textSize(box_size)
    fill(0)
    ligne = 0
    text("Nombres de comparaisons (ce tour) : " + comparaisons, padding + 2* largeur_canvas / 5, padding + ligne * hauteur_ligne)
    ligne++
    text("Nombres de comparaisons (total) : " + comparaisons_total[position+1], padding + 2*largeur_canvas / 5, padding + ligne * hauteur_ligne)

}