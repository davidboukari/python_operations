from apps.exception import ExceptDivisionByZero


def somme(nombre_1: int, nombre_2: int) -> int:
    """
    :param nombre_1: number to add
    :type nombre_1: int
    :param nombre_2: number to add
    :type nombre_2: int
    :return: return the sum ot the nombre_1 + nombre_2
    :rtype: int
    """
    return nombre_1 + nombre_2


def soustraction(nombre_1: int, nombre_2: int) -> int:
    """
    :param nombre_1: number
    :type nombre_1: int
    :param nombre_2: number to substract
    :type nombre_2: int
    :return: return the substraction ot the nombre_1 - nombre_2
    :rtype: int
    """
    return nombre_1 - nombre_2


def multiplication(nombre_1: int, nombre_2: int) -> int:
    """
    :param nombre_1: number
    :type nombre_1: int
    :param nombre_2: number
    :type nombre_2: int
    :return: return the substraction ot the nombre_1 * nombre_2
    :rtype: int
    """
    return nombre_1 * nombre_2


def division(nombre_1: int, nombre_2: int):
    if nombre_2 == 0:
        return 'Error'
    else:
        return nombre_1 / nombre_2


def division_with_exception(nombre_1: int, nombre_2: int):
    try:
        return nombre_1 / nombre_2
    except Exception:
        raise ExceptDivisionByZero
