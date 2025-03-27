n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))
if n1==n2==n3:
    print('São todos Iguais!')
else:
    if n1>n2:
        if n1>n3:
            print(n1, 'é o maior!')
        else:
            if n1==n3:
                print('n1 e n3 são iguais')
            else:
                print(n3, 'é o maior!')
    else:
        if n2>n3:
            print(n2, 'é o maior!')
        else:
            if n2==n3:
                print('n2 e n3 são iguais')
            else:
                print(n3 , 'é o maior!')
