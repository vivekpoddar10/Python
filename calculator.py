def main():
    x = int(input('Enter a number: '))
    print(f'{x} square is {square(x)}')

def square(n):
    return n * n

if __name__ == '__main__':
    main()