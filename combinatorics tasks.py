import itertools

# Задача 1: размещения по 5 элементов
def task1(alphabet, length):
    permutations = list(itertools.permutations(alphabet, length))
    with open('1.txt', 'w') as file:
        for perm in permutations:
            file.write(''.join(map(str, perm)) + '\n')
        file.write(f'Количество элементов: {len(permutations)}\n')

# Задача 2: слова длины 7 с одним символом, который повторяется 3 раза, и одним символом, который повторяется 2 раза
def task2(alphabet):
    words = set()
    for num1 in alphabet:
        for num2 in alphabet:
            if num1 != num2:

                base_word = [num1] * 3 + [num2] * 2

                for remaining in alphabet:
                    if remaining != num1 and remaining != num2:
                        for perm in itertools.permutations(base_word + [remaining]):
                            words.add(''.join(map(str, perm)))
    
    with open('2.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')

# Задача 3: слова длины 6, в которых 3 символа 2
def task3(alphabet):
    words = set()
    count_2 = 3
    base_word = [2] * count_2 

    for remaining in itertools.product(alphabet, repeat=3):

        if all(r != 2 for r in remaining):
            for perm in itertools.permutations(base_word + list(remaining)):
                words.add(''.join(map(str, perm)))

    with open('3.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')


alphabet = [1, 2, 3, 4, 5, 6, 7, 8]

task1(alphabet, 5)
task2(alphabet)
task3(alphabet)