initial_input = input().split()

def list_of_even_numbers(one_list):
    final_input = []
    for current_digit in initial_input:
        if int(current_digit) % 2 == 0:
            final_input.append(current_digit)
    result = ', '.join(final_input)
    return result


print(f'[{list_of_even_numbers(initial_input)}]')
