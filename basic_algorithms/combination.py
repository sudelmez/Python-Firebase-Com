def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)    

def comb(num,many):
    value = fact(num)/(fact(num-many)*fact(many))
    return value

print(comb(5,2))    