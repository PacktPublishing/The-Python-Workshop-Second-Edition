d1 = dict(key1="d1", key3="d1")
d2 = dict(key2="d2", key3="d2")
print(d1 | d2)

d1 = dict(key1="d1", key3="d1")
d1 |= dict(key2="d2", key3="d2")
print(d1)
