import random

sides = 6

def main():
    dice1= random.randint(1 , sides)
    dice2= random.randint(1 , sides)

    print(f"First die {dice1}")
    print(f"Second die {dice2}")
    print(f"There total sum {dice1 + dice2}")

if __name__ == '__main__':
    main()