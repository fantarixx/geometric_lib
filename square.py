def area(a):
    '''The function returns the area of a square.
    Parameters:
        a : a number representing the side length of the square
    Returns:
        a * a : the square of the number 'a', which equals the area of a square with side 'a'
    '''
    if a <= 0:
        raise ValueError("The side of the square cannot be negative.")
    return a * a


def perimeter(a):
    '''The function returns the perimeter of a square.
    Parameters:
        a : a number representing the side length of the square
    Returns:
        4 * a : the product of the number 'a' and 4, which equals the perimeter of a square with side 'a'
    '''
    if a <= 0:
        raise ValueError("The side of the square cannot be negative.")
    return 4 * a
