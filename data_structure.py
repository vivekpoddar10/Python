import json

'''
***********************************************************************************************
* Dictionaries in Python
***********************************************************************************************
'''

my_dict = {'first_name':'vivek', 'last_name':'Poddar'}

#fetching value stored in respect of key
print(my_dict['first_name'])
print(my_dict['first' + '_name'])

''''
***********************************************************************************************
* Adding new key-value in object
***********************************************************************************************
'''
my_dict['profession'] = 'Engineer'
my_dict['friends'] = ['Siddharth', 'Ashish', 'Vishal']
print(json.dumps(my_dict, indent=2))

print(f'{my_dict['first_name']} has {len(my_dict['friends'])} friends')

