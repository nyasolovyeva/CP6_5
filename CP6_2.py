def vvod(M, N): # функция ввода массива
    for i in range(N):
        M[i] = round(randint(-10,10),1)
    print(M)

def obsh(M, N): # функция нахождения общих элементов
    for i in M: # номер прохода 
        for j in N: # просмотр за один проход
            if i == j: # если элементы равны
                print(i)

from random import randint
N1 = int(input("Введите размерность массива 1: "))
D = [0] * N1 # заполнение массива нулями
vvod(D, N1)

N2 = int(input("Введите размерность массива 2: "))
A = [0] * N2 # заполнение массива нулями
vvod(A, N2)
obsh(D, A)