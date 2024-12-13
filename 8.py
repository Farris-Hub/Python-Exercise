total = 0
for i in range(2, 11, 2):
    print(i, end=" ")
    if i < 10:
        print("+", end=" ")
    total += i
print(f"= {total}")