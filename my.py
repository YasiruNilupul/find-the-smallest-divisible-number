k=0
num=1
while True:
    for i in range(1,21):
        if num%i!=0:
            break
        else:
            k+=1
        
    if k==20:
        print(num)
        break
    k=0
    num+=1

