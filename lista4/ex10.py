n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero"))
if n1<n2:
    n1=n1*10
    n2=n2/2
    n1= n1+n2
    if n1 % 2 == 0:
        print("Par")
    else:
        print("Impar")
else:
    if n2<n1:
        n2 = n2*10
        n1 = n1/2
        n2 = n1+n2
        if n2 % 2 == 0:
            print("Par")
        else:
            print("Impar")

        
