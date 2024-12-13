numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
total = sum(numbers)
average = total / len(numbers)
print(f"Sum = {total}, Average = {average}")