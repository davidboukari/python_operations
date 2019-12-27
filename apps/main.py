from apps.exception import ExceptDivisionByZero
from apps.operation import somme, soustraction, multiplication, division, division_with_exception


def main():
    """
    Read the fist number
    """
    first_number = int(input('Enter a number: '))

    """
    Read the fist number
    """
    second_number = int(input('Enter a second number: '))

    """
    Call somme()
    """
    somme_two_number = somme(first_number, second_number)
    print(f'{first_number} + {second_number} = {somme_two_number}')

    """
    Call subraction()
    """
    substraction_two_number = soustraction(first_number, second_number)
    print(f'{first_number} - {second_number} = {substraction_two_number}')

    """
    Call multiplication()
    """
    multiplication_two_number = multiplication(first_number, second_number)
    print(f'{first_number} * {second_number} = {multiplication_two_number}')

    """
    Call division()
    """
    division_two_number = division(first_number, second_number)
    print(f'{first_number} / {second_number} = {division_two_number}')

    """
    Call division_with_exception()
    """
    try:
        division_two_number_with_exception = division_with_exception(first_number, second_number)
        print(f'{first_number} / {second_number} = {division_two_number_with_exception}')
    except ExceptDivisionByZero:
        print('Division by zero')


"""
in main call function main()
"""
if __name__ == '__main__':
    main()
