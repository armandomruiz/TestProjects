import csv
from itertools import permutations
#esta funcion calcula las permutaciones del vector dado y las guarda en un archivo
def compute_permutations(vector, filename):
    perms = permutations(vector)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(perms)

import math
#esta funcion filtra las permutaciones que cumplen las condiciones: 1.- Incluyen dos nueves y 2.- El último elemento es un número primo
#También se guardan en un archivo csv
def filter_permutations(input_file, output_file):
    prime_permutations = []

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            permutation = list(map(int, row))
            if is_prime2(permutation[-1]):
                if permutation.count(9) == 2:
                    prime_permutations.append(permutation)
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(prime_permutations)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_prime2(num):
    if num < 2:
        return False
    elif num == 2 or num == 3 or num == 5 or num == 7:
        return True

vector = [0, 0, 2, 2, 3, 4, 4, 8, 8, 9, 9]
filename = 'permutations.csv'
compute_permutations(vector, filename)

output_file = 'filtered_permutations.csv'
filter_permutations(filename, output_file)

