table_multiplication = int(input("Entrer une table de multiplication entre 1 et 9."))

if(table_multiplication > 9):
    input("Vous devez entrer une table de multiplication entre 1 et 9.")
else:
    i = 0
    for i in range(1, 11):
        table = i * table_multiplication
        print(i, "x" , table_multiplication, "=" , table)