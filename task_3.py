from random import randint

def get_unique_list_numbers(start = -10, stop = 10, lenght = 16) -> list[int]:
    list_ = []
    while len(list_) < lenght:
        rand_sym = randint(start,stop)
        if rand_sym not in list_:
            list_.append(rand_sym)
        return list_



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
