# Michał Wełna 302935

from typing import List
import random, sys
from timeit import timeit
sys.setrecursionlimit(1500)

def partition(lst: List[int], begin :int, end:int) -> int:
    pivot = begin
    for i in range(begin,end):
        if lst[i] < lst[end]:
            lst[i], lst[pivot] = lst[pivot], lst[i]
            pivot +=1
    lst[pivot], lst[end] = lst[end], lst[pivot]

    return pivot


def quick_tmp_sort(lst: List[int], begin: int, end: int) -> None:
        if begin < end:
            place = partition(lst, begin, end)
            quick_tmp_sort(lst, begin, place - 1)
            quick_tmp_sort(lst, place + 1, end)


def quicksort(lst: List[int]) -> [int]:
    lst_tmp = lst[:]
    quick_tmp_sort(lst_tmp, 0, len(lst_tmp) -1)

    return lst_tmp



def bubblesort(lst: List[int]) -> (List[int], int):
    tmp = lst[:]
    counter = 0
    for i in range(len(tmp) - 1,0,-1):
        is_sorted = True
        for j in range(i):
            counter +=1
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
                is_sorted = False
        if is_sorted:
            result = tmp, counter
            return result
    result = tmp, counter
    return result


lst1 = [x for x in range(1,1001)]
lst2 = [x for x in range(1000,0,-1)]
lst3 = 1000 * [5]
lst4 = random.sample(range(1,2000),1000)
lst5= [5,7,3,8,2,1,33,4]
print(quicksort(lst5))

t1_bubble = timeit('bubblesort(lst1)', number = 1, globals = globals())
t1_qsort = timeit('quicksort(lst1)', number = 1, globals = globals())

t2_bubble = timeit('bubblesort(lst2)', number = 1, globals = globals())
t2_qsort = timeit('quicksort(lst2)', number = 1, globals = globals())

t3_bubble = timeit('bubblesort(lst3)', number = 1, globals = globals())
t3_qsort = timeit('quicksort(lst3)', number = 1, globals = globals())

t4_bubble = timeit('bubblesort(lst4)', number = 1, globals = globals())
t4_qsort = timeit('quicksort(lst4)', number = 1, globals = globals())

#Sprawdzamy dzialania algorytmow dla utworzonych 4 list powyzej
#Dla listy uporzadkowanej (posortowanej):
print('Lista posortowana:')
print('Czas bubblesort:', t1_bubble )
print('Czas quicksort:', t1_qsort)
#Wniosek: Dla od razu uporzadkowanej listy algorytm bubble_sort jest znacznie szybszy od quick_sorta
#Teraz dla listy malejacej od 1000 do 1:
print('Lista malejaca od 1000 do 1:')
print('Czas bubblesort:', t2_bubble )
print('Czas quicksort:', t2_qsort )
#Po czasach wnioskujemy, ze quick_sort poradzil sobie z tym nieco szybciej od bubble_sorta
print('Lista skladajaca sie z tysiaca elementow o takiej samej wartosci (w tym przypadku 1000 * 5:')
print('Czas bubblesort:', t3_bubble)
print('Czas quicksort:', t3_qsort)
#Wniosek: dla listy zlozonej z takich samych elementow - bubble_sort jest wydajniejszy
print('Lista skladajaca sie z 1000 randomowych liczb:')
print('Czas bubblesort:', t4_bubble)
print('Czas quicksort:', t4_qsort)
#Dla przypadku zupelnie losowego w kazdym z przypadkow szybszy okazal sie algorytm quicksort
#WNIOSEK: Dla przypadkow zupelnie losowych oraz w najgorszych przypadkach zdecydowanie wydajnieszy jest algorytm quick_sort
#Jednak istnieja przypadki szczegolne, dla ktorych lista jest juz posortowana badz sklada sie z tych samych elementow, wtedy lepszy okazuje sie bubble_sort
