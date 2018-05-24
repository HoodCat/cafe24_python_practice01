num = int(input('숫자를 입력하세요: '))

num_list = list(filter(lambda value: value % 2 == 0, range(0, num+1))) \
    if num % 2 == 0 \
    else list(filter(lambda value: value % 2 != 0, range(0, num+1)))

print(f'결과 값 : {sum(num_list)}')
