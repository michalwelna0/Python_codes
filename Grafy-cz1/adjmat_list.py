#Michał Wełna 302935
from typing import List, Dict

def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dct = {}
    for index, elem in enumerate(adjmat,1):
        lst =[]
        for index2, elem2 in enumerate(elem,1):
            if elem2 !=0:
                for i in range(elem2):
                     lst.append(index2)
        if lst:
            dct[index] = lst

    return dct


def dfs_recursive(g: Dict[int, List[int]], s: int) -> List[int]:
    already_visited = []
    def dfs_recursive2(b: Dict[int, List[int]], z: int, visited_list: List[int]) -> List[int]:
        visited_list.append(z)
        for neigh in b[z]:
            if neigh not in visited_list:
                dfs_recursive2(b,neigh,visited_list)
        return visited_list

    return dfs_recursive2(g,s,already_visited)



def dfs_iterative(g: Dict[int, List[int]], s: int) -> List[int]:
    stack,lst = [s],[]

    while stack:
        elem = stack.pop()
        if elem not in lst:
            lst.append(elem)
        for neigh in reversed(g[elem]):
            if neigh not in lst:
                stack.append(neigh)
    return lst


def dfs_iterative_help(g: Dict[int, List[int]], s: int) -> bool:
    stack,lst = [s],[]

    while stack:
        elem = stack.pop()
        if elem not in lst:
            lst.append(elem)
        for neigh in reversed(g[elem]):
            if neigh not in lst:
                stack.append(neigh)
            elif g[neigh]:
                return False
    return True


def is_acyclic(g: Dict[int, List[int]]) -> bool:
    lst = list(g.keys())
    for i in lst:
        result = dfs_iterative_help(g,i)
        if result is False:
            return False
    return True

A = [
    [0, 1],
    [0, 0],
]
print(adjmat_to_adjlist(A))

G = {
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]
}
print(dfs_iterative(G,1))
print(dfs_recursive(G,1))

W1 = {1: [2, 3], 2: [], 3: [4], 4: []}
W2 = {1: [2], 2: [3], 3: [1]}
W3 = {1: [], 2: [1, 3], 3: [2]}
W4 = {1: [2], 2: [], 3: [2, 4], 4: [3]}
W5 = {1: [2, 3], 2: [4], 3: [4], 4: []}
W6 = {1: [2, 3], 2: [3], 3: []}
W7 = {1: [2], 2: [3], 3: [1, 4], 4: []}
print(is_acyclic(W1))
print(is_acyclic(W2))
print(is_acyclic(W3))
print(is_acyclic(W4))
print(is_acyclic(W5))
print(is_acyclic(W6))
print(is_acyclic(W7))

