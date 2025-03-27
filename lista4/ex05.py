n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero:"))
n3 = int(input("Digite um numero:"))
if n1==n2==n3:
    print('Numeros iguais!')
else:
    if n1>n2:
        if n1>n3:
            menor = n1+5
            print(menor,'n1')
        else:
            if n1==n3:
                print('Tente com numeros diferentes!')
            else:
                menor = n3+5
                print(menor, 'n3')
    else:
        if n1==n2:
            print('Tente com numeros diferentes!')
        else:
            if n2<n3:
                menor = n2+5
                print(menor, 'n2')
            else:
                if n2==n3:
                    print('Tente com numeros diferentes')
                else:
                    menor = n3+5
                    print(menor, 'n3')
                        
