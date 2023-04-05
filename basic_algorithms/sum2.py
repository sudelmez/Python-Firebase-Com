def sum(num):
    total=0    
    for i in range(0,num+1):
        total+=i
    return total

sayi=int(input("Sayi Giriniz: "))
print("Sayi Toplamı: ",sum(sayi))
