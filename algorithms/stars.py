def MakeStars(num):
    for i in range(num+1):
        print("*"*i + "  "*(num-i) + "*"*i)

MakeStars(5)        