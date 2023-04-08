n = int(input("End:"))

count = 0

for i in range(1,n+1):
    while(i > 0):
        digit = i % 10
        count+=1
        i = i // 10

print(count)


