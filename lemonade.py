bills=[5,5,5,10,20]
def billchange(bills):
    fb=0
    tb=0
    for i in bills:
        if i==5:
            fb+=1
        elif i==10:
            if fb>0:
                fb-=1
                tb+=1
            else:
                return False
        else:
            if tb>0 and fb>0:
                tb-=1
                fb-=1
            elif fb>=3:
                fb-=3
            else:
                return False
    return True

print(billchange(bills))