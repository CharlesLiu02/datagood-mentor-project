"""def generator():
    current = 'a'
    while current <= 'z':
        yield current
        current = chr(ord(current)+1)

for x in generator():
    print (x)
"""

def rev_generator():
    current = "z"
    while current >= "a":
        yield current
        current = chr(ord(current) - 1)
"""
for x in rev_generator():
    print(x)"""

print(next(rev_generator()))
