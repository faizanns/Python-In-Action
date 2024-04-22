import os, random

names = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
cnt = 0
while cnt < 5:
    dir_name = random.choice(names)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    cnt = 0
    for n in names:
        for directory in os.listdir():
            if directory == n:
                cnt += 1