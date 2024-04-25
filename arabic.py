# Change original to be the alphabet you want for example
# original = ['a', 'b', 'c', 'd', 'e', 'f']

# This just spawns 180 consecutive hexadecimal numbers, comment it and replace with your alphabet
original = [hex(i) for i in range(1,181)]


# DO NOT CHANGE ANYTHING BELOW

def reverse(a):
    if len(a) == 0:
        return []
    elif len(a) == 1:
        return a
    else:
        return reverse(a[1:-1]) + [a[len(a)-1], a[0]]

prev = original
new = reverse(original)
count = 1

while new != original:
    print(f"Row: {count} -> {prev}")
    prev = new
    new = reverse(prev)
    count += 1

print(f"Row: {count} -> {prev}")
print(f"Row: {count+1} -> {new}")
