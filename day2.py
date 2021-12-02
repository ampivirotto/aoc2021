h = 0
d = 0

with open("day2input.txt") as f:
    for line in f:
        temp = line.split(" ")
        if temp[0] == 'forward':
            h += int(temp[1])
        elif temp[0] == 'up':
            d -= int(temp[1])
        elif temp[0] == 'down':
            d += int(temp[1])

print(h, d)
print(h * d)

h2 = 0
d2 = 0
aim = 0

with open("day2input.txt") as f:
    for line in f:
        temp = line.split(" ")
        if temp[0] == 'forward':
            h2 += int(temp[1])
            d2 += int(temp[1]) * aim
        elif temp[0] == 'up':
            aim -= int(temp[1])
        elif temp[0] == 'down':
            aim += int(temp[1])

print(h2, d2)
print(h2 * d2)