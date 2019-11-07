subsid = int(input())
count = int(input())
for b in range(1, subsid // 20 + 1):
    for k in range(subsid // 10 + 1):
        for t in range(subsid // 5 + 1):
            if b*20 + k*10 + t*5 == subsid and b + k + t == count:
                print(b, k, t)
                
           
