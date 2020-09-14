cnt     = 0
row     = 1
line    = 1

while cnt < 2014:
    row ^= row << 1
    cnt += '{:b}'.format(row).count('0')
    line += 1
print(line)
