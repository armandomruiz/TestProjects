import csv
#revisa la primera condicion
def check_eights(vector):
    for i in range(len(vector) - 1):
        if vector[i] == '8' and vector[i+1] == '8':
            return True
    return False
#revisa la segunda condicion
def check_nines(vector):
    nines = [i for i, num in enumerate(vector) if num == '9']

    for i in range(len(nines) - 1):
        start = nines[i] + 1
        end = nines[i+1]

        numbers_between_9s = vector[start:end]
        unique_numbers = set(numbers_between_9s)

        if len(numbers_between_9s) != len(unique_numbers):
            return False

    return True
#revisa la tercera condicion
def condition_three(vector):
    if '8' not in vector:  # Check if '8' is present in the vector
        return False

    index_of_eight = vector.index('8')  # Find the index of the first occurrence of '8'

    left_numbers = set(vector[:index_of_eight])  # Extract the numbers to the left of '8'
    right_numbers = set(vector[index_of_eight + 1:])  # Extract the numbers to the right of '8'

    common_numbers = left_numbers.intersection(right_numbers)  # Find the common numbers between the left and right sides

    if len(common_numbers) >= 2:  # Check if there are at least two common numbers
        return True

    return False
#revisa la cuarta condicion
def check_threes(vector):
    for i in range(len(vector)):
        if vector[i] == '3':
            if i == 0 or i == len(vector) - 1:
                return False

            prev_num = vector[i - 1]
            next_num = vector[i + 1]

            if prev_num != next_num:
                return False

    return True
import math
#revisa la quinta condicion
def check_divisible_elements(vector):
    if len(vector) < 8:
        return False

    num_5 = int(vector[4])
    num_6 = int(vector[5])
    num_7 = int(vector[6])

    if num_5 == 0 or num_6 == 0 or num_7 == 0:
        return False
    gcd = math.gcd(math.gcd(num_5, num_6), num_7)
    if gcd == 1:
        return False
    if num_5 % gcd == 0 and num_6 % gcd == 0 and num_7 % gcd == 0:
        return True
    else:
        return False
#revisa la sexta condicion
def check_second_last_divisible(vector):
    if len(vector) >= 2:
        second_last = int(vector[-2])
        last = int(vector[-1])

        if last != 0:
            if second_last % last == 0:
                return True

    return False
#revisa la ultima condicion
def check_prime(vector):
    if len(vector) >= 1:
        last_number = int(vector[-1])

        if last_number >= 2:
            if last_number == 2:
                return True

            if last_number % 2 == 0:
                return False

            for i in range(3, int(last_number ** 0.5) + 1, 2):
                if last_number % i == 0:
                    return False
            
            return True

    return False
#funcion que recibe de entrada un conjunto de permutaciones y una lista vacia donde se guardaran aquellas que cumplan
#todas las condiciones impuestas
def check_conditions_from_file(filename,permutations_found):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            permutation = row
            print(permutation)
            if check_zero_four(permutation) and check_eights(permutation) and check_nines(permutation) and condition_three(permutation) and check_threes(permutation) and check_divisible_elements(permutation) and check_second_last_divisible(permutation) and check_prime(permutation):
                permutations_found.append(permutation)
                #return permutation

    return None
#funcion para ver si un número es primo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
#funcion que revisa si el vector comienza con 0 y 4 en ese orden.
def check_zero_four(vector):
    if len(vector) != 11:
        return False
    
    if vector[0] == '0' and vector[1] == '4':
        return True
    
    return False

permutations_found=[]

filename = 'filtered_permutations.csv'
#result = check_conditions_from_file(filename)
check_conditions_from_file(filename,permutations_found)
print(permutations_found)
#print(result)
