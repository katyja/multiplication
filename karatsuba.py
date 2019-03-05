BASE = 10


def split_number_at(operand, split_at):
    """
    split number at the split_at
    >>> operand = 342312
    >>> a, b = split_number_at(542312, 2)
    high operand
    >>> a == 542
    low operand
    >>> b == 312
    :param operand: operand to split
    :param split_at: number of digit where to split
    :return: high and low operand
    """
    return divmod(operand, BASE**split_at)


def multiplication(operand1, operand2):
    """
    main function for multiplication operand
    :param operand1: first operand
    :param operand2: second operand
    :return: multiplication operand1 * operand2
    """
    if operand1 < BASE and operand2 < BASE:
        return operand1*operand2
    maximum_size = max(len(str(operand1)), len(str(operand2)))
    split_size = divmod(maximum_size, 2)[0]
    a, b = split_number_at(operand1, split_size)
    c, d = split_number_at(operand2, split_size)
    z2 = multiplication(a, c)
    z0 = multiplication(b, d)
    z1 = multiplication(a + b, c + d)
    return z2*BASE**(2*split_size) + ((z1 - z2 - z0)*BASE**split_size) + z0


if __name__ == '__main__':
    print(multiplication(1111,
                         2222))
