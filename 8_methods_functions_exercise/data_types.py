first_input = input()
second_input = input()


def data_type(type, value):
    if type == "int":
        return(2 * int(value))
    elif type == "real":
        return(f'{1.5 * float(value):.2f}')
    elif type == "string":
        return(f'${value}$')


print(data_type(first_input, second_input))