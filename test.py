import numpy as np

# Сигмоида
def nonlin(x, deriv = False):
    if (deriv == True):
        return x * ( 1 - x )
    return 1 / ( 1 + np.exp( -x ) )

# набор входных данных
X = np.array([  [1, 0, 1],
                [1, 1, 1],
                [1, 0, 1],
                [0, 1, 1] ])

# выходные данные
y = np.array([[0, 1, 1, 0]]).T

# сделаем случайные числа более определёнными
#np.random.seed(1)

# инициализируем веса случайным образом со средним 0
#syn0 = np.random.random((3, 1))

syn0 = [[ 9.67299686],
        [-0.20801528],
        [-4.62953613]]



print(syn0)
print()

for iter in range(1):

    # прямое распространение
    l0 = X
    l1 = nonlin( np.dot(l0, syn0) )

    # насколько мы ошиблись?
    #l1_error = y - l1

    # перемножим это с наклоном сигмоиды
    # на основе значений в l1
    #l1_delta = l1_error * nonlin(l1, True) # !!!

    # обновим веса
    #syn0 += np.dot(l0.T, l1_delta) # !!!

print("Выходные данные после тренировки:")
print(l1)
print()
print(syn0)
