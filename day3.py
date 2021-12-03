import pandas as pd 
import numpy as np

def leastmode(val):
    if val == '1':
        return '0'
    else:
        return '1'

def mode(tblcol):
    ones = list(tblcol).count('1')
    zeros = list(tblcol).count("0")
    if ones >= zeros:
        return '1'
    elif ones < zeros:
        return '0'

codes = {}

counter = 0
with open("day3input.txt") as f:
    for line in f:
        codes[counter] = list(line.strip("\n"))
        counter+=1

df = pd.DataFrame.from_dict(codes, orient = 'index')


x = df.mode().iloc[0]

gastr = "".join(x)

epstr = ""
for i in x:
    epstr += leastmode(i)

gamma = int(gastr, 2)
epi = int(epstr, 2)

print(gamma * epi)

temp = df
newmode = mode(temp[0])
for i in range(len(x)):
    temp = temp[temp[i] == newmode]
    if len(temp) == 1:
        break 
    newmode = mode(temp[i+1])
o2 = int("".join(temp.iloc[0]), 2)


temp = df
newmode = leastmode(mode(temp[0]))
for i in range(len(x)):
    temp = temp[temp[i] == newmode]
    if len(temp) == 1:
        break 
    newmode = leastmode(mode(temp[i+1]))
co2 = int("".join(temp.iloc[0]), 2)
print(o2 * co2)
