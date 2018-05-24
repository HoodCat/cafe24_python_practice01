num_list = list(map(str, range(1, 100)))

for num in num_list:
    for char in '369':
        if char in num:
            print(f'{num}: 짝')
            break
