def get_int():
    while True:
        try:
            num = int(input('Please enter an integer: '))
        except ValueError:
            pass #print(f'Invalid input')
        else:
            return num #break
        
        '''
        try:
            return int(input(prompt))
        except ValueError:
            pass
        '''
            
    

def main():
    x = get_int()
    print(x)

if __name__ == '__main__':
    main();