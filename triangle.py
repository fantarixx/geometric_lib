def area(a, b, c):
    '''The function returns the semi-perimeter of a triangle.
    Parameters:
        a, b, c : the three sides of the triangle
    Returns:
        (a + b + c) / 2 : the semi-perimeter of the triangle
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("The sides of a triangle cannot be negative.")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The sides do not form a triangle.")
    return (a + b + c) / 2


def perimeter(a, b, c):
    '''The function returns the perimeter of a triangle.
    Parameters:
        a, b, c : the three sides of the triangle
    Returns:
        a + b + c : the perimeter of the triangle
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("The sides of a triangle cannot be negative.")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The sides do not form a triangle.")
    return a + b + c
