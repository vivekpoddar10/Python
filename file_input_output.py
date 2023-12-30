# name = input('what\'s your name? ')
# fname = input('what\'s your father\'s name? ')

# file = open('name.txt', 'a')
# file.write(name + '\n')
# file.close()

# with open('name.txt', 'a') as file:
#     file.write(f'{name}\n')

# with open('name.txt', 'r') as file:
#     for line in file:
#         print(f'Hello,', line.rstrip())

# with open('name.txt', 'r') as file:
#     lines = file.readlines()
#     lines.sort()

# for _ in lines:
#     print(_.rstrip())

# with open("name.txt", "r") as file:
#     for line in sorted(file, reverse=True):
#         print(line.rstrip())

# with open("name.txt", "r") as file:
#     lines = file.readlines()
#     for line in range(len(lines)):
#         if lines[line].rstrip() == 'Vivek Poddar':
#             print(f'exist in the file, at line {line+1}')
#             break
#     else:
#         print('not found')

# with open("name.txt", "r") as file:
#     for line in file:
#         if line.rstrip() == 'Vivek Poddar':
#             print(f'exist in the file')
#             break
#     else:
#         print('not found')

# with open('names.csv', 'a') as file:
#     file.write(f'{name},{fname}\n')

import json
students = []
with open('names.csv', 'r') as file:
    for line in file:
        name, fname = line.rstrip().split(',')
        student = {'name': name, 'father':fname}
        students.append(student)

print(json.dumps(student, indent=2))