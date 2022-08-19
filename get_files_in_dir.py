print('go')
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('https://losst.ru/'):
    f.extend(filenames)
    print(dirnames)
    break