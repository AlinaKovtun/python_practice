s = "aaasdf ss"
print({i:s.count(i) for i in set(s)})
#{'a': 4, 'd': 3, 'k': 3, 's': 3, 'l': 4}