import random

while True:
    start = 1
    end = 100
    answer = random.randint(start, end)
    print('수를 결정하였습니다. 맞추어 보세요')
    count = 0

    while True:
        count += 1
        print(f'{start}-{end}')
        num = int(input(f'{count}>> '))
        if num > answer:
            print('더 낮게')
            end = num
        elif num < answer:
            print('더 높게')
            start = num
        else:
            print('맞았습니다.')
            break

    retry = input('다시 하시겠습니까(y/n)>> ')
    if retry == 'n':
        break
