# Create an array
def simple_arrays():
    print("Creating an array with a = ['IM_SAMPLE_DATA']")
    a = ["i'm element 1"]
    print(f'Array, a, created and looks like this--->{a}')

    # Adding to an array
    print(f'add second element to array with a.append(IM_SAMPLE_DATA)')
    a.append("I'm #2")
    print(f'Arraya, a, now looks like this--->{a}')
    print('Adding and then deleting a third one')
    a.append("I'm #3")
    print(f'Arraya, a, now looks like this--->{a}')
    a.pop(2)
    print(f'Arraya, a, now looks like this--->{a}')

    print(f"\n Let's loop through the array")
    for element in a:
        print(f"I'm in the array--->{element}")
