data=" 1 10 2 ".strip().split()
i=int(data[0])
r=int(data[1])
k=int(data[2])

count=0
for j in range(i,r+1):
    if j%k==0:
        count+=1
print(count)