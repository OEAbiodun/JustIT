# list = ['Apple', 'Orange', 'Banana', 'Kiwi']

# if ('Banana' in list):
#     print('Your selection is in the list.')
# else:
#     print('No selection in the list')

list = ['Apple', 'Orange', 'Banana', 'Kiwi']
choice = str(input('Check You Favourite Fruit:  '))

if (choice in list):
    print(f'Your selection {choice} is in the list.')
else:
    print(f'{choice} is not in the list')