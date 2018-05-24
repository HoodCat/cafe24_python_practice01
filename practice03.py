s = '/usr/local/bin/python'

print(str(s.split('/')[1:])[1:-1])
print(str(s.rsplit('/', 1))[1:-1])
