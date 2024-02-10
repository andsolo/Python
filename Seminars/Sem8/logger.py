from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор? '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')




def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))


    print('2 файл:')    
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

def redone_data():
    var = int(input(f'В какой базе вы бы хотели заменить данные?\n'
                    f'1 - Первая база\n'
                    f'2 - Вторая база\n\n'
                    f'Ваш выбор? '))
    
    old_data = input('Какое слово или значение Вы бы хотели заменить? ')
    new_data = input('На какое слово или значение Вы бы хотели его поменять? ')

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            search_data = file.read()

        replace_data = search_data.replace(old_data, new_data)

        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(replace_data)
    
    else:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            search_data = file.read()

        replace_data = search_data.replace(old_data, new_data)

        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(replace_data)