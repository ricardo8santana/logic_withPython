idade = int(input("Qual a sua idade?"))

if idade >= 18:
    print("Entrada liberada!")
elif idade == 16 or idade == 17:
    acompanhante = input("Possui acompanhante?")
    if acompanhante == "sim":
        print("entrada Liberada")
    else:
        print("Entrada Negada")
else:
   print("Entrada Negada")