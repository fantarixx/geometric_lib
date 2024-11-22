import math

def area(r):
    '''The function returns the area of a circle.
    Parameters:
        r : the radius of the circle
    Returns:
        math.pi * r * r : the area of the circle
    '''
    if r <= 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * r * r

def perimeter(r):
    '''The function returns the circumference of a circle.
    Parameters:
        r : the radius of the circle
    Returns:
        2 * math.pi * r : the circumference of the circle
    '''
    if r <= 0:
        raise ValueError("The radius cannot be negative.")
    
    return 2 * math.pi * r
