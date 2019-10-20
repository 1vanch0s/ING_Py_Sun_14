# 20 30 50 40 -1 2 -10 8 13
total_min = 9999999999999999999
total_max = -99999999999999999
i = 0
while i < 5:
    num = int(input("Enter number: "))
    if num < total_min:
        total_min = num
    if num > total_max:
        total_max = num
    i += 1

print("Total min is ", total_min)
print("Total max is ", total_max)
    
