import datetime
my_dict = {}

my_dict[1] = 'I exist'
my_dict[2] = 'second entry'

#checking if a key exists
def my_function(id, my_dict):
    if id in my_dict:
        print(f'\t{my_dict[1]}')
    else:
        print(f'\tNo key {id} found in my_dict')

print("When key exists:")
my_function(1,my_dict)
print("When key does NOT exist:")
my_function(10,my_dict)
print(f'Arraya, a, now looks like this--->{a}')

print(f'Print all items with my_dict.items:\n {my_dict.items()}')
print(f'Print all keys with my_dict.items:\n {my_dict.keys()}')
