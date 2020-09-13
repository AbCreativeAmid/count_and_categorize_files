def makeArrayConsecutive2(statues):
    complete_status = list(range(min(statues),max(statues)+1))
    return len(complete_status)-len(statues)
a = [6, 2, 3, 8]
print(makeArrayConsecutive2(a))