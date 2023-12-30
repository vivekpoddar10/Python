import sys

# print(f'Hi my name is {sys.argv[1]}')

# if len(sys.argv) > 2:
#     sys.exit('Too many arguments')
# elif len(sys.argv) < 2:
#     sys.exit('Too few argument')

# print(f'hello, {sys.argv[1]}')

try:
    print(sys.argv[1])
except (ZeroDivisionError, IndexError):
    print('Invalid')
