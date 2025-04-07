import math

def main():
    Base = float(input("Enter the length of base of the triangle: "))
    Perpendicular = float(input("Enter the length of perpendicular of the triangle: "))

    Hypotenuse = float(math.sqrt( Base**2 + Perpendicular**2))

    print(f"The length of Hypotenuse is {Hypotenuse}")

if __name__ == '__main__':
    main()