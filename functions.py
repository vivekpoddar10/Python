# input functions
name = input('What\'s your name?').strip().title();
print(f'Hello, {name}') # default parameter: string, sep=" ", end="\n"
arr = name.split(' ')
print(arr);