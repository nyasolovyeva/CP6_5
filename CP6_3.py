def minel(M): # функция нахождения индекса минимального элемента массива
    min_el = M[0]
    for i in range(1, len(M)): # перебор индексов, начиная со второго элемента
        if M[i] < min_el:
            min_el = M[i]
    return min_el

def sr_delta(M):
    k = 0
    for i in range(len(M)): # перебор индексов
        if M[i] - min_el == delta: 
            k += 1
    print(k)

delta = int(input("Введите delta: "))
A = [4, 6, 6, 2, 9]


min_el = minel(A) # вызываем функцию minel
sr_delta(A)
