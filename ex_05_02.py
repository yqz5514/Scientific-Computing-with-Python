

smallest = None
for vl in [3, 44, 5, 66, 77, 12, 45, 7]:
    if smallest is None:
        smallest = vl
    elif vl < smallest:
        smallest = value

print('smallest:', smallest)
