import re

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
s = s.upper()
words = list(set(re.split('[.,\n ]', s)))
words.remove('')
words.sort()

# 1)
for word in words:
    print(word)

# 2)
for word in words:
    print(f'{word}:{s.count(word)}')