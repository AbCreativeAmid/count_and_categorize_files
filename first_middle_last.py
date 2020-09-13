def mix(s1,s2):
    res = s1[:1]+s2[:1]
    res += ((s1[len(s1)//2]) + (s2[len(s2)//2]))
    res +=s1[-1]+s2[-1]
    return res
print(mix("America","Japan"))