def my_function(a):
    ms = a  * 365 * 24 * 60 * 60 * 100
    return ms

age = int(input())

if age % 2 == 0:
    seconds = my_function(age)
else:
    print("Kek")

###########

i = 15
while i <= 30:
    seconds = my_function(i)
    print(seconds)
    i = i + 1


################
print(my_function(43))
