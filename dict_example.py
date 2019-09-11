import datetime
def simple_dict():
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

    print(f'Print all items with my_dict.items:\n {my_dict.items()}')
    print(f'Print all keys with my_dict.items:\n {my_dict.keys()}')

    for key, value in my_dict.items():
        print(f"Key is {key} and item is {value}.")
