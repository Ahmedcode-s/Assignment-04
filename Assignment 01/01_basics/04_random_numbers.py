import random

total_numbers : int = 10
min_value : int = 1
max_value : int = 100

def main():
    for i in range(total_numbers):
        num = random.randint(min_value, max_value)
        print(num)

if __name__ == '__main__':
    main()