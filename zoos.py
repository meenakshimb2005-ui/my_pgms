word="zzoooo".strip()
x=0
y=0

for i in word:
    if i=="z":
        x+=1
    elif i=="o":
        y+=1
        
if 2*x==y:
    print("yes")
else:
    print("no")