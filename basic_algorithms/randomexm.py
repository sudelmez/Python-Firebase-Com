import random

rand= random.randint(0,20)
num=int(input("sayi giriniz: "))
while(num != rand):
    num=int(input("sayi giriniz: "))

    if(rand>num):
        print("küçük oldu. Tekrar deneyin...")
        continue
    elif(rand<num):
        print("büyük oldu. Tekrar deneyin...")

    else:
        break

print("Doğru tahmin!")
