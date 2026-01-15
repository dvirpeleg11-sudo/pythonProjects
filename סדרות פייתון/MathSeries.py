import math

def input_deteails_for_serie():
    a1 = int(input("Enter a1: "))
    q = int(input("Enter q: "))
    n = int(input("Enter n: "))
    return a1, q, n

def create_serie(a1,q, n):
    serie = [a1]

    for i in range(n - 1):
        serie.append(serie[len(serie) - 1] * q)
    return serie

def get_a_value(serie, a1, q):
    n = int(input("Enter the n value you want to get: "))
    value = a1 * math.pow(q, n - 1)
    return value

def get_q(serie, a1, n):
    q = serie[1] / a1

    for i in range(1, len(serie) - 1):
        if serie[i+1] / serie[i] != q:
            print("Its not an engeneering serie")
            return None
    return q

def sum_serie(serie, q):
    a1 = int(input("Enter the first value for the sum: "))
    n = int(input("Enter the numbers of values for the sum: "))
    var_sum_serie = (a1 * (math.pow(q, n - 1) - 1)) / (q - 1)
    return var_sum_serie

def is_engeneer(serie, a1, n):
    if get_q(serie, a1, n) != None:
        return True
    else:
        return False

def print_serie(serie):
    for x in serie:
        print(x)

def choosing_function(serie, a1, q, n):
    var_get_a_value = 1
    var_get_q = 2
    var_sum_serie = 3
    var_is_engeneer = 4
    var_print_serie = 5
    exit = 6
    var_choosen_function = 0

    while var_choosen_function != exit:
        print("""
for getting a particular value in the n position - Enter 1,
for getting the q, enter 2,
for sum from a to a - Enter 3
for getting true or false if the siere is engeneered - Enter 4
for printing the serie - Enter 5
for exiting - Enter 6
        """)
        var_choosen_function = int(input())

        if var_choosen_function == 1:
            res = get_a_value(serie, a1, q)
            print(res)
        elif var_choosen_function == 2:
            res = get_q(serie, a1, n)
            print(res)
        elif var_choosen_function == 3:
            res = sum_serie(serie, q)
            print(res)
        elif var_choosen_function == 4:
            res = is_engeneer(serie, a1, n)
            print(res)
        elif var_choosen_function == 5:
            print_serie(serie)
        elif var_choosen_function != 6:
            print("Not a valid choice")

    print("you quited to loop. thanks for participating! see you next time...")

def main():
    a1, q, n = input_deteails_for_serie()
    serie = create_serie(a1, q, n)
    choosing_function(serie, a1, q, n)

main()