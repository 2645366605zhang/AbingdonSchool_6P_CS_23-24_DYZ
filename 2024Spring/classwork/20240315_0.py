print("Enter integer (0-99) :")
Value = int(input())
print("Calculate additive or multiplicative persistence (a or m) ?")
Operation = input()

count = 0
while Value > 9:
    if Operation == "a":
        Value = (Value // 10) + (Value % 10)
    else:
        Value = (Value // 10) * (Value % 10)
    count += 1
print("The persistence is:")
print(count)

