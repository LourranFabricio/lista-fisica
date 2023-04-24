def pi(termo):
    base = 1
    num = 0
    for i in range(1, termo+1):
        if(i == 1):
            num = 1/base
            

        if(i % 2 != 0 and i != 1):
            base += 2
            num += 1/base
            

        if(i % 2 == 0):
            base+=2
            num -= 1/base
            
    return num*4

print(pi(10))
print(pi(100))
print(pi(1000))
