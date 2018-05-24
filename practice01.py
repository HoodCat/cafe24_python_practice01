num = input()

if not num.isdigit():
    print('정수가 아닙니다.')
    exit(0)

num = int(num)

if num % 3 == 0:
    print('3의 배수 입니다.')
else:
    print('3의 배수가 아닙니다.')
exit(0)
