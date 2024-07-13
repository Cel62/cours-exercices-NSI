from PIL import Image

img_initiale = Image.open("img/lena.jpg")


taille = img_initiale.size
print("Largeur ", taille[0], "px")
print("Hauteur ", taille[1], "px")

img_finale = img_initiale.convert('L')

img_finale.save('img/lena_ndg.png')

img_initiale.close()
img_finale.close()