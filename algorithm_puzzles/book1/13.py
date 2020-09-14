from itertools import permutations

#num1 =  'read'
#num2 = 'write'
#num3 =  'talk'
#num4 = 'skill'
#
#1) s, t, w, r != 0
#2) d + e + k % 10 = l
#3) a + t = 8 or  9 or 10
#4) e + a = 8 or 9 or 10
#5) s = w + 1 or w + 2

def genNum(*args):
    out = 0
    for num in args:
        out *= 10
        out += num
    return out

cnt = 0
for (a, d, e, k, l, t) in permutations(range(10), 6):
    if 8 <= a + e <= 10 and 8 <= a + t <= 10 and (d + e + k) % 10 == l:
        tmp = [el for el in range(10) if el not in (a, d, e, k, l, t)]
        for (i, r, s, w) in permutations(tmp, 4):
            if r != 0 and t != 0 and w != 0 and s != 0 and w + 1 <= s <= w + 2:
                num1 = genNum(r, e, a, d)
                num2 = genNum(w, r, i, t, e)
                num3 = genNum(t, a, l, k)
                num4 = genNum(s, k, i, l, l)
                
                if num1 + num2 + num3 == num4:
                    cnt += 1
                    print("{} + {} + {} = {}".format(num1, num2, num3, num4))
print(cnt)
