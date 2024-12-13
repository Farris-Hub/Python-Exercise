total = 0
for i in range(1, 6):
    if i < 5:
        print(f"{i} +", end=" ")
    else:
        print(i, end=" ")
    total += i
print(f"= {total}")