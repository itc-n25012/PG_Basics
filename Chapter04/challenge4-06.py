# Challenge4-01
def f(x):
    """
    A function that takes a number as input
    and returns the square of that number.
    :param x: int.
    :return:: x squrared.
    """
    return x ** 2

print(f(2))
print(f(3)) 

# Challenge4-02
def print_string(string):
    """
    A function that takes a string as an
    argument and outputs that string.
    :param string: str.
    """
    print(string)

print_string("Python")

# Challenge4-03
def f(x, y, z, a=10, b=20):
    """
    A function with three required and two
    optional arguments.
    :parm x: int.
    :parm y: int.
    :parm z: int.
    :parm a: int.
    :parm b: int.
    :return: First add x, y, and z, them multiply by a and b.
    """
    return (x+y+z)*a*b

result = f(1, 2, 3)
print(result)

# Challenge4-04
def divide(x):
    """
    A function that takes an integer as an
    argument and divides that integer by 2.
    :parm x: int.
    :return: x divided by 2.
    """
    return x / 2

def multiply(x):
    """
    A function that takes an integer as an
    argument and returns the ineger
    multiplied by 4.
    :parm x: int.
    :return: x multiplied by 4
    """
    return x * 4

a = divide(10)
b = multiply(a)

print(b)

# Challenge4-05
def conv(string):
    """
    A function that converts a string to a
    float type and returns the result
    :parm string: str.
    :return: Convert a string to a float. 
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert")

s = float("3.14")
print(s)
