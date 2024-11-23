def fatorial(n):

    fat = 1

    if n == 1 and n ==0:
        fat = 1
        print(fat)
    elif n < 0:
        print('Não existe fatorial de número negativo')
    else:
        while n > 1:
            fat = fat * n
            n = n - 1
        return fat

    
fatorial(int(input('Fatorial:')))

def numero_binomial(n,k):
    if k <= n and k >= 0 and n >= 0:
        bin = (fatorial(n)) / ((fatorial(k)) * (fatorial(n-k)))
        return bin
    else:
        print('k é maior do que n')

numero_binomial(int(input('n:')),int(input('k:')))
