num_list = list(filter(lambda num: num%3==0, range(10, 30)))
print(f'주어진 리스트에서 3의 배수의 개수 => {len(num_list)}')
print(f'주어진 리스트에서 3의 배수의 합 => {sum(num_list)}')
