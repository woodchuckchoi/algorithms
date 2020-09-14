Countries = ["bl", "ca", "mo", "cn", "sn", "ns", "ce", "aa", "ca", "ge", "ce", "jn", "uy", "ca", "ed", "iy", "sd", "er", "fe", "hs", "aa", "ba", "in", "na", "gy", "pl", "ga", "ua", "bm", "aa", "ra", "kc"]

def wordTail(leftCountries, log):
    if len(log) != 0:
	    flag = False
	    
	    for leftCountry in leftCountries:
	        if log[-1][-1] == leftCountry[0]:
	            flag = True
	            break
	
	    if not flag:
	        return 0

    maxCountry = 0
    for idx, leftCountry in enumerate(leftCountries):
        if len(log) != 0:
            if leftCountry[0] != log[-1][-1]:
                continue
        copied = leftCountries[:]
        copied.pop(idx)
        cnt = 1 + wordTail(copied, log+[leftCountry])
        maxCountry = max(maxCountry, cnt)

    return maxCountry

print(wordTail(Countries, []))
    
    
