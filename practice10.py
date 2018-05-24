menu = input('메뉴: ')

menu_price = {'오뎅':300,
              '순대':400,
              '만두':500}

print(f'가격: {menu_price.get(menu, 0)}')
