# # input functions
# name = input('What\'s your name?').strip().title();
# print(f'Hello, {name}') # default parameter: string, sep=" ", end="\n"
# arr = name.split(' ')
# print(arr);
'''
def main():
    myFunc()


def myFunc():
    print('This is my first function')

if __name__ == '__main__':
    main()
'''

def calcAge(year):
    return 2023 - year

def calcRetirementTime(year, name):
    age = calcAge(year)
    retireAge = 65 - age
    if retireAge > 0:
        print(f'{name} will retire after {retireAge} years')
    else:
        print(f'{name} has already retired')
    
if __name__ == '__main__':
    calcRetirementTime(2020, 'vivek')
