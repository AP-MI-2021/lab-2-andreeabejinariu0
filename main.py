'''
Găsește ultimul număr prim mai mic decât un număr dat.
'''
def prime(nr):
    if nr < 2:
        return False
    for i in range (2 , nr):
        if nr % i == 0:
            return False
    return True
def get_largest_prime_below (nr):
    for i in range (nr-1, 1, -1):
        if prime(i) == True:
            return i
            break
    return False
def test_get_largest_prime_below():
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(112) == 109
    assert get_largest_prime_below(41) == 37
    assert get_largest_prime_below(225) == 223
    assert get_largest_prime_below(-4) == False

from datetime import datetime as dt
def get_age_in_days(birthdate):
    data2 = dt.today().strftime('%d/%m/%Y') #converteste data de azi
    birthdate = dt.strptime(birthdate, '%d/%m/%Y')#converteste data de nastere intr-un sir de caractere
    azi = dt.strptime(data2, '%d/%m/%Y')
    zile = birthdate - azi#diferenta de zile
    return (abs(zile.days))#diferenta in modul exprimata in zile
def get_goldbach(n):
    if n % 2 == 1:
        return None
    for p1 in range(1, n // 2, +2):
        if prime(p1):
            p2 = n - p1
            if prime(p2):
                return p1, p2
                break
def test_get_goldbach():
    assert get_goldbach(18) == (5 , 13)
    assert get_goldbach(14) == (3, 11)
    assert get_goldbach(42) ==(5, 37)
    assert get_goldbach(20) == (3, 17)
    assert get_goldbach(45) == None
def main():
    while True:
        print('1. Găsește ultimul număr prim mai mic decât un număr dat.')
        print('2. Varsta persoanei in zile')
        print('3. Conjunctura lui Goldbach')
        print('x. Iesirea din program - exit')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            nr = int(input('Dati un numar: '))
            if get_largest_prime_below(nr):
                print(f'Ultimul numar prim mai mic decat {nr} este ',get_largest_prime_below(nr))
            else:
                print(f'Nu exsita numar prim mai mic decat {nr}.')
        elif optiune == '2':
            data1 = str(input("Introduceti data nasterii: (dd/mm/yyyy)"))
            print('Numarul zilelor este de ',get_age_in_days(data1))
        elif optiune == '3':
            n = int(input('Dati un numar: '))
            print(get_goldbach(n))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')
test_get_largest_prime_below()
test_get_goldbach()
main()
