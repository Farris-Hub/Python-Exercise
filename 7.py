total = 0
for i in range(1, 6, 2):
    print(i, end=" ")
    if i < 5:
        print("+", end=" ")
    total += i
print(f"= {total}")