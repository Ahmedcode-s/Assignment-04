max_value = 10000

def main():
    a = 0
    b = 1
    print(a,b, end = " ")

    while True:
        c = a + b
        if c >= max_value:
            break
        print(c, end=" ")
        a = b
        b = c

if __name__ == "__main__":
    main()

