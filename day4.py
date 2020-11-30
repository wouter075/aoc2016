from collections import Counter

# open file
with open("day4.txt") as file:
    lines = [line.strip() for line in file]

ids = 0
# read file, line by line
for l in lines:
    # fill in all the details
    sp = l.split("-")
    sector = sp[-1:][0].split("[")[0]
    checksum = sp[-1:][0].split("[")[1][:-1]
    letters = "".join(sp[:-1])

    # print
    print(letters)
    # print(sector)
    print(checksum)

    # magic
    ll = Counter(letters)
    max = ll[checksum[:1]]
    a = True
    for x in checksum:
        if ll[x] <= max:
            max = ll[x]
        else:
            a = False
            break
    if a:
        ids += int(sector)
    print("-"*20)


print(f"The anweser is: {ids}")
