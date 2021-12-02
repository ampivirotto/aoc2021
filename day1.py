
num_in = 0
depths = []

with open("day1_input.txt") as f:
    for line in f:
        depth = int(line.strip("\n"))
        depths.append(depth)

        if len(depths) > 1:
            if depth > prevd:
                num_in += 1
        prevd = depth
print(num_in)

win_incr = 0
first = 0
second = 0
third = 0

counter = -1
with open("day1_input.txt") as f:
    for line in f:
        if counter == -1:
            first += int(line)
        elif counter == 0:
            first += int(line)
            second += int(line)
        elif counter == 1:
            first += int(line)
            second += int(line)
            third += int(line)
        elif counter == 2:
            second += int(line)
            if second > first:
                win_incr += 1
            first = int(line)
            third += int(line) 
        elif counter == 3:
            third += int(line)
            if third > second:
                win_incr += 1
            second = int(line)
            first += int(line)
        elif counter == 4:
            first += int(line)
            if first > third:
                win_incr += 1
            third = int(line)
            second += int(line)
            counter = 1
        counter += 1

print(win_incr)
