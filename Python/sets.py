#criar set
s = set()
print(f"The set has {len(s)} elements.")
#add items no set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print(s) #{1,2,3,4}

s.remove(2)
print(s) #{1,3,4}

print(f"The set has {len(s)} elements.")

