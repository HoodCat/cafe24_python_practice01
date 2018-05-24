num_list = []
for i in range(5):
    num_list.append(int(input('> ')))

print(f'평균: {sum(num_list)/len(num_list)}')