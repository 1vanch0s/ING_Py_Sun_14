A = int(input())
B = int(input())
sign = input()
while True:
    if sign == "+" :
        print(A + B)
        break
    elif sign == "-" :
        print(A - B)
        break
    elif sign == "*" :
        print(A * B)
        break
    elif sign == "/" :
        if B != 0 :
            print( A / B)
        else:
            print("ЫЫЫЫЫЫ")
        break
        
    else: 
        print("ЫЫЫЫЫЫ")
        break
