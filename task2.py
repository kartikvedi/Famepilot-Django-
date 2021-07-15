import math
def solve():
    a = int(input("Enter the coefficients of a: "))
    b = int(input("Enter the coefficients of b: "))
    c = int(input("Enter the coefficients of c: "))
    # discriminant
    d = b ** 2 - 4 * a * c
    #This discriminant will never be lessthan zero as it is given in question that there
    #always exists a solution
    if d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return (x,x)
    else:
        x1 = (-b + math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        x2 = (-b - math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        return (x1,x2)
print(solve())