n1 = int(input("Digite um numero:"))
if n1>10:
    n1 = n1+5
    if n1>25:
        print("Numero maior que dez,e atingiu",n1)
    else:
        print("numero maior que dez, mas não atingiu 25.")
else:
    if n1<= 10:
        n1 = n1+20
        if n1>25:
            print("Numero menor ou igual a 10, mas atingiu ", n1)
        else:
            n1<=25
            print("Numero menor que 10, não atingiu 25")
