n = int(input('Digite um número inteiro: '))

primo = True

if n==2:
    print('primo')
elif n==1:
    print('não primo')
else:
    j = n - 1
    while j > 1:
        if n%(j)==0:
            primo = False
            break
        j = j - 1


if primo and n!=1 and n!=2:
    print('primo')
else:
    if n!=2 and n!=1:
        print('não primo')

    
  
    
    

