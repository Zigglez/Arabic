# Change original to be the alphabet you want for example
# original = ['a', 'b', 'c', 'd', 'e', 'f']

# This just spawns 180 consecutive hexadecimal numbers, comment it and replace with your alphabet
original = [hex(i) for i in range(1,181)]

م ح م د ا د م ا ب ر ا ه ي م ي و س ف د ا و د س ل ي م ن ع ي س ى ك ي و م ر ث ج م ش ي د ف ر ي د و ن ك س ر ي س ك ن د ر ن و ش ي ر و ا ن م و س ى س ا ج د ن و ر ج ح ا ن ز ه ل م ش ت ر ي م ر ي خ ش م س ز ه ر ة ع ط ا ر د ق م ر ج ب ر ا ا ي ل م ي ك ا ا ي ل ا س ر ا ف ي ل ع ز ر ا ا ي ل د ر د ا ا ي ل ر ف ت م ا ا ي ل م ي ط ط ر و ن

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
