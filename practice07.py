money = int(input('금액:'))

if money // 50000 > 0:
    print(f'50000원 : {money//50000}개')
    money = money % 50000

if money // 10000 > 0:
    print(f'10000원 : {money//10000}개')
    money = money % 10000

if money // 5000 > 0:
    print(f'5000원 : {money//5000}개')
    money = money % 5000

if money // 1000 > 0:
    print(f'1000원 : {money//1000}개')
    money = money % 1000

if money // 500 > 0:
    print(f'500원 : {money//500}개')
    money = money % 500

if money // 100 > 0:
    print(f'100원 : {money//100}개')
    money = money % 100

if money // 50 > 0:
    print(f'50원 : {money//50}개')
    money = money % 50

if money // 10 > 0:
    print(f'10원 : {money//10}개')
    money = money % 10

if money // 5 > 0:
    print(f'5원 : {money//5}개')
    money = money % 5

if money // 1 > 0:
    print(f'1원 : {money}개')
